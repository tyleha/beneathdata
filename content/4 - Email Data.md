Title: Visualize your email activity with Pandas
Date: 2016-1-2 16:25
Tags: email, gmail, python, pandas, personal data
Category: How-to
Slug: visualize-email-history
Author: Tyler Hartley

You'll need a few basic python packages to follow this tutorial, namely `numpy`, `matplotlib` and `pandas`. If you don't already have these data analysis packages, I'd suggest taking a look at [Anaconda](https://www.continuum.io/downloads).

All this code will be written for Python 3.4+, executed in IPython. There are a few tweaks you'd have to make to get this working in 2.7, and I'll call them out where applicable.[ref]But you should migrate to 3.x already. It's been 8 years. Shame on you.[/ref]

## fetching emails and parsing

While this tutorial will specifically focus on accessing emails from Gmail, it should broadly apply to almost any email provider. That's because Gmail, like pretty much everybody else, supports the IMAP access protocol

### Get emails over IMAP

IMAP is pretty straightforward. Select a mail folder, retrieve a list of email ids that match a query string, and then fetch the content of those emails by id.

Unfortunately, it's a bit tricky to do cleanly and performantly, so I've quickly abstracted a class to handle the low-level fetching and parisng for you. To follow this tutorial, copy my [`GmailAccount` class](https://gist.github.com/tylerhartley/fe00a92d01346b29b002) into your project someplace.[ref]You could totally use the pretty decent [gmail package](https://github.com/charlierguo/gmail) instead of my own, but a) it hasn't been updated in years and b) it is waaaaaaay overkill for what we're doing.[/ref] 


### Convert your emails into a DataFrame

Great! We've fetched thousands of emails (probably). But they're in an unworkable format. This is where [pandas](http://pandas.pydata.org/) comes into play. If you've read any of my [previous]() [blogs](), you'll know what a True Believer I am in pandas. There's no better way to work with data in Python and you may find you never write a `for` loop again.[ref]Also your code looks really organized and terse, which is nice.[/ref] 

```python
import numpy as np
import pandas as pd
```

All we need to do is reformat our emails into a nice array of key/value pairs for pandas to load. Each email object has a `_headers` list containing each field we requested in our IMAP fetch query. So this function should do the trick:

```python
def scrub_email(headers):    
    d = {}
    for val in headers:
        # IMAP sometimes returns fields with varying capitalization...
        d[val[0].lower()] = val[1]
    return d
```

Now load your emails into a `DataFrame`.

```python
df = pd.DataFrame([scrub_email(email._headers) for email in received])
```

### Parse RFC dates into pandas Timestamps

Remaining problem: the `date` field in our emails unusable to us. We need to parse the string literal into a knowledgable python object, and pandas provides us just such a class: `Timestamp`. Now, I have my beef with a few things about `Timestamp`, but it does a great job combining the functionality of a bunch of different python modules[ref]Datetime, pytz, and emailutils.parse, to name a few.[/ref] into one cohesive unit. 

Now, if you simply wanted to work with each timestamp from the perspective of a single timezone, this would be _super_ easy. Just `df['timestamp'] = pd.Timestamp(df.date)`. Dang. Even add `utc=True` to convert everything to UTC. But as you'll see below, I actually want timezone _naive_ timestamps, and that gets a little trickier.

## Analysis

So now the question is: what do we want to ask of our email data? To me, email is a uniquely dense log of our social interactions. Phone calls are too sparse. Text messages capture only a subset of my closest contacts. But email...everybody emails. So I was curious what email could tell me about my daily habits. 

To visualize daily email, let's break down emails by hour of the day sent or received, and plot that over time. Since there are probably tens of thousands of emails in your inbox (over 100,000 in mine), a simple scatter plot will saturate too easily. This looks like a job for a heatmap.

But first, we'll have to tackle that timezone naive problem I mentioned before. I want to know when I sent emails in _local_ time. If I was in Seattle and I sent an email at 17:00 PST, I want to register that as 17:00, not 20:00 EST or 01:00 UTC. And when am on the east coast, I want 17:00 EST to register as 17:00, not 14:00 PST or 22:00 UTC. Problem is, pandas makes it [nigh impossible to work with multiple timezones in a single Series](http://stackoverflow.com/a/17027507/1766755). So we'll need to bash this problem with a `datetime` hammer.

```python
def try_parse_date(d):
    try:
        ts = pd.Timestamp(d)

        # IMAP is very much not perfect...some of my emails have no timezone
        # in their date string. ¯\_(ツ)_/¯
        if ts.tz is None: 
            ts = ts.tz_localize('UTC')

        # I moved from east coast to west coast in 2010, so automatically assume EST/PST 
        # before/after that date.
        if ts < pd.Timestamp('2010-09-01', tz='US/Eastern'):
            ts = ts.tz_convert('US/Eastern')
        else:
            ts = ts.tz_convert('US/Pacific')
        # Here's the magic to use timezone-naive timestamps
        return pd.Timestamp(ts.to_datetime().replace(tzinfo=None))
    
    except:
        return np.nan
``` 

For my dataset of 100k emails, that handled all but 72 of them, which we'll ignore. Sometimes, IMAP just has dates formatted in a totally irregular way, like `Thursday , 10 Dec 2009 16:28:55, +0000 GMT`. Not worth the effort.

Let's apply `try_parse_date` and label our data by month to facilitate later grouping.

```python
freq = 'M' # could also be 'W' (week) or 'D' (day), but month looks nice.
# The line below might take a minute...
df['timestamp'] = df.date.map(lambda x: try_parse_date(x))
df = df.dropna(subset=['timestamp'])

# This converts our DataFrame index to be a timestamp DatetimeIndex array which
# is *highly* performant to work with.
df = df.set_index('timestamp', drop=False)
# I want to bin my data by month. Use pandas Period class to do this.
df.index = df.index.to_period(freq)
```

Now, for each period (month), we'll need count the number of emails received each hour of the day. If that sounds like at least 3 for loops and a lot of boilerplate code, you haven't used pandas `value_counts()`:

```python
df['hour'] = df.timestamp.map(lambda x: x.hour)

mindate = df.timestamp.min()
maxdate = df.timestamp.max()
pr = pd.period_range(mindate, maxdate, freq=freq)

# Initialize a new HeatMap dataframe where the indicies are actually Periods of time
# Size the frame anticipating the correct number of rows (periods) and columns (hours in a day)
hm = pd.DataFrame(np.zeros([len(pr), 24]) , index=pr)

for period in pr:
    # HERE'S where the magic happens...with pandas, when you structure your data correctly, it can be so terse that
    # you almost aren't sure the program does what it says it does...
    # For this period (month), find all emails within this month and count how many emails were received
    # within each hour of the day in that month. Wow. Takes more words to explain than to code.
    if period in df.index:
        hm.ix[period] = df.loc[[period]].hour.value_counts()
    
# If for some weird reason there was ever an hour period where you had no email,
# fill those NaNs with zeros.
hm.fillna(0, inplace=True)
```

### compute occurrences of each hour
### plot using pcolor

## go further
### most frequently contacted people
### monthly distinct recipients




TODO
* fix email
* fix share buttons (where'd they go!?)
* figure out if publishing an edit triggers rss

