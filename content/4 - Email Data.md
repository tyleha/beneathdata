Title: Visualize your email activity with Pandas
Date: 2016-1-2 16:25
Tags: email, gmail, python, pandas, personal data
Category: How-to
Slug: visualize-email-history
Author: Tyler Hartley

You'll need a few basic python packages to follow this tutorial, namely `numpy`, `matplotlib` and `pandas`. If you don't already have these data analysis packages, I'd suggest taking a look at [Anaconda](https://www.continuum.io/downloads).

All this code will be written for Python 3.x, and executed in an IPython (Jupyter) notebook. There are a few tweaks IPython you'd need to make to get this working in 2.7, and I'll call them out where applicable.[ref]But you should really start using 3.x for data analysis already. It's been 8 years. Shame on you.[/ref]

Here's my import list for this tutorial:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.gridspec as gridspec
from datetime import timedelta, datetime, date

import GmailAccount # my package
```

<br>
## Step 1: Get your emails and parse them

While this tutorial will specifically focus on accessing emails from Gmail, it should broadly apply to almost any email provider. That's because Gmail, like pretty much everybody else, supports the IMAP access protocol

### Getting email content via IMAP

IMAP is pretty straightforward. Select a mail folder, retrieve a list of email ids that match a query string, and then fetch the content of those emails by id. 

Unfortunately, it's a bit tricky to do cleanly and performantly, so I've quickly abstracted a class to handle the low-level fetching and parisng for you. To follow this tutorial, copy my **[GmailAccount class](https://gist.github.com/tylerhartley/fe00a92d01346b29b002)** into your project someplace, which under the hood just uses Python's `imaplib` and `email`.[ref] You could totally use this pretty decent [gmail package](https://github.com/charlierguo/gmail) instead of my own, but a) it hasn't been updated in years and b) it is waaaaaaay overkill for what we're doing.[/ref] I won't be getting into any real specifics about how to best use `imaplib`, so feel free to dig around the class to learn more.

**BEFORE YOU START:** a while back, Gmail disabled basic auth (non Oauth2) access to raw IMAP. Oauth-ing into your inbox is well beyond the scope of this tutorial and I mean, this isn't an IPhone app so, I suggest you just [allow less secure apps to login to your account](https://www.google.com/settings/security/lesssecureapps). That way, you just need your email address and password to use IMAP. Don't forget to turn less secure access back off when you're done.

OK - let's login to Gmail and fetch metadata 'bout all our emails:

```python
gmail = GmailAccount(username='you@gmail.com', password=password)
gmail.login()

daysback = 6000 # ~10yrs...make this whatever ya like
notsince = 0 # since now.
since = (date.today() - timedelta(daysback)).strftime("%d-%b-%Y")
before = (date.today() - timedelta(notsince)).strftime("%d-%b-%Y")

SEARCH = '(SENTSINCE {si} SENTBEFORE {bf})'.format(si=since, bf=before)
ALL_HEADERS = '(BODY.PEEK[HEADER.FIELDS (DATE TO CC FROM SUBJECT)])'

# Search and fetch emails!
received = gmail.load_parse_query(search_query=SEARCH, 
                                  fetch_query=ALL_HEADERS, 
                                  folder='"[Gmail]/All Mail"')
```

Preeeeety simple with the `GmailAccount` class! 

Before we move on, let's quickly break down that `ALL_HEADERS` string. It describes the fields we're requesting from the mail server and info about how we want them. We want fields that can be found in the email header (`HEADER.FIELDS`). Of those fields, we just want a few (`DATE TO CC FROM SUBJECT`). Importantly, we want to `PEEK` at those emails so as to not mark any of them read and wipe out any unread counts you have in your inbox.[ref]Alternatively, feel free to remove `PEEK` and mark all your emails as read...looking at you Mr. 8,127 unread...[/ref] 




### Converting your emails into a DataFrame

Great! We've fetched thousands of emails (probably). But they're in an unworkable format. This is where [pandas](http://pandas.pydata.org/) comes into play. If you've read any of my [previous]() [blogs](), you'll know what a True Believer I am in pandas. There's no better way to work with data in Python and you may find you never write a `for` loop again.[ref]Also your code looks really organized and terse, which is nice.[/ref] 

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

Luckily, the `GmailAccount` class took care of parsing the raw email payload into a useful format courtesy of `email.parser`. Try `received[-1]['Subject']` and you should see the subject of the most recent email in your inbox!

A remaining problem: the `date` field in our emails is unusable to us. It's just a dumb string. We need to parse it into a knowledgable python object, and pandas provides us just such a class: `Timestamp`. Now, I have my beef with a few things about Timestamp, but it does a great job combining the functionality of a bunch of different python modules[ref]Datetime, pytz, and emailutils.parse, to name a few.[/ref] into one cohesive unit. 

Now, if you simply wanted to work with each timestamp from the perspective of a single timezone, this would be _super_ easy. Just `df['timestamp'] = pd.Timestamp(df.date)`. Dang. Even add `utc=True` to convert everything to UTC. But as you'll see in the next section, I actually want timezone _naive_ timestamps, and that gets a little trickier.

<br>
## Step 2: Analysis and visualization

So now the question is: what do we want to ask of our email data? To me, email is a uniquely dense log of our social interactions. Phone calls are too sparse. Text messages capture only a subset of my closest contacts. But email...everybody emails. So I was curious what email could tell me about my daily habits. 

To visualize daily email, let's break down emails by hour of the day sent or received, and plot that over time. Since there are probably tens of thousands of emails in your inbox (over 100,000 in mine), a simple scatter plot will saturate too easily. This looks like a job for a heatmap.

### Prepare data

But first, we'll have to tackle that timezone naive problem I mentioned before. I want to know when I sent emails in _local_ time. If I was in Seattle and I sent an email at 17:00 PST, I want to register that as 17:00, not 20:00 EST or 01:00 UTC. And when am on the east coast, I want 17:00 EST to register as 17:00 too, not 14:00 PST or 22:00 UTC. Problem is, pandas makes it [nigh impossible to work with multiple timezones in a single Series](http://stackoverflow.com/a/17027507/1766755). So we'll need to bash this problem with a `datetime` hammer.

```python
# Parse date strings remaining naive across multiple timezones
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
        # If we fail, return NaN so pandas can remove this email later.
        return np.nan

df['timestamp'] = df.date.map(try_parse_date)
# Remove any emails that Timestamp was unable to parse
df = df.dropna(subset=['timestamp'])
``` 

For my dataset of 100k emails, that handled all but 72 of them, which I'm not going to lose much sleep over. Sometimes, IMAP just has dates formatted in a totally irregular way, like `Thursday , 10 Dec 2009 16:28:55, +0000 GMT`. Not worth the effort. 

Obviously, this timezone approach above this misses a few outliers like distant vacations, but this approach is plenty accurate for my purposes. If you don't need to handle emails sent in different timezones (maybe you've never left the Eastern timezone, I dunno), then you can skip a lot of the mess and just do:

```python
# Alternate date parse function for only one timezone
def try_parse_date(d):
    try:
        ts = pd.Timestamp(d)
        if ts.tz is None: 
            ts = ts.tz_localize('UTC')
        return ts.tz_convert('Your Timezone Here') 
    except:
        return np.nan
```

To build our heatmap, we'll need to know two things about each email

1. Hour of the day the email was sent (local time) 
1. Year-Month in which the email was sent

Getting hour is easy:

```python
df['hour'] = df.timestamp.map(lambda x: x.hour)
```

Voila. To get an email's month, we can very quickly convert any `Timestamp` to any particular period of time with pandas `Period` class.

```python
freq = 'M' # could also be 'W' (week) or 'D' (day), but month looks nice.
df = df.set_index('timestamp', drop=False)
df.index = df.index.to_period(freq)
```

Fast. Simple. To see what happened, take a look at your DataFrame with `tail()`:

```python
In [35]: df.tail()
Out[35]: 
            cc                             date 
timestamp                                         
2015-12    NaN  Thu, 31 Dec 2015 02:07:11 +0000   
2015-12    NaN  Wed, 30 Dec 2015 18:12:44 -0800   
2015-12    NaN  Wed, 30 Dec 2015 18:16:31 -0800   
2016-01    NaN  Fri, 01 Jan 2016 18:20:06 -0800   
2016-01    NaN  Sat, 02 Jan 2016 01:03:22 -0500  
```

The Period (month) of each date is now the DataFrame index! This is actually a really critical step for a couple reasons. First, we now have super easy slicing and grouping of our data - just try selecting a particular month of interest with the `ix` indexer:

```python
In [36]: df.ix[pd.Period('2015-12', 'M')]
Out[36]: 
            cc                             date 
timestamp                                         
2015-12    NaN  Thu, 31 Dec 2015 02:07:11 +0000   
2015-12    NaN  Wed, 30 Dec 2015 18:12:44 -0800   
2015-12    NaN  Wed, 30 Dec 2015 18:16:31 -0800 
...
```

The second reason is that by setting a series of `Period`s as our DataFrame index, pandas automatically converted it to a `PeriodIndex` class for us which is super, super fast and easy to remap to a different timezone or slice (as we saw above). As it turns out, a series of plain `Period`s is actually incredibly non-performant to slice. #TODO improve this paragraph

### Build heatmap DataFrame

Our email DataFrame now contains all the info we need to build our heatmap. Now, for each month, we'll need count the number of emails received each hour of the day for each month. If that sounds like a few `for` loops and a lot of boilerplate code, you haven't used pandas' `value_counts()`:

```python
mindate = df.timestamp.min()
maxdate = df.timestamp.max()
pr = pd.period_range(mindate, maxdate, freq=freq)
# Initialize a new HeatMap dataframe where the indicies are actually Periods of time
# Size the frame anticipating the correct number of rows (periods) and columns (hours in a day)
hm = pd.DataFrame(np.zeros([len(pr), 24]) , index=pr)

for period in pr:
    # HERE'S where the magic happens...with pandas, when you structure your data correctly, 
    # it can be so terse that you almost aren't sure the program does what it says it does...
    # For this period (month), find relevant emails and count how many emails were received in
    # each hour of the day. Takes more words to explain than to code.
    if period in df.index:
        hm.ix[period] = df.ix[[period]].hour.value_counts()

# If for some weird reason there was ever an hour period where you had no email,
# fill those NaNs with zeros.
hm.fillna(0, inplace=True)
```

Just to prove a point, you could actually do the above with zero `for` loops using `groupby` and `pivot`, but this actually looks cleaner to me.

### Plot heatmap using `pcolor`

There are a lot of ways to plot heatmaps in matplotlib, from `scatter` to `imshow` to `pcolor`. I like `pcolor`. 

We already created our matrix of values, `hm`, and all that's left is to plot and format our axes. 

```python
### Set up figure
fig = plt.figure(figsize=(12,8))
# This will be useful laterz
gs = gridspec.GridSpec(2, 2, height_ratios=[4,1], width_ratios=[20,1],)
gs.update(wspace=0.05)

### Plot our heatmap
ax = plt.subplot(gs[0])
x = dates.date2num([p.start_time for p in pr])
t = [datetime(2000, 1, 1, h, 0, 0) for h in range(24)]
t.append(datetime(2000, 1, 2, 0, 0, 0)) # add last fencepost
y = dates.date2num(t)
cm = plt.get_cmap('Oranges')
plt.pcolor(x, y, hm.transpose().as_matrix(), cmap=cm)

### Now format our axes to be human-readable
ax.xaxis.set_major_formatter(dates.DateFormatter('%b %Y'))
ax.yaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
ax.set_yticks(t[::2])
ax.set_xticks(x[::12])
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([t[0], t[-1]])

### Add a colorbar!
plt.colorbar(cax=plt.subplot(gs[1]))
```

While we're at it, let's add a line plot of total emails received per month:

```python
g = df.groupby(level=0)
total_email = g.hour.count()

ax2 = plt.subplot(gs[2])
plt.plot_date(total_email.index, total_email, '-', linewidth=1.5, color=cm(0.999))
ax2.get_xaxis().set_visible(False)
ax2.get_yaxis().set_visible(False)
```

#### Image here

Now if we start from the top, change the selected Gmail inbox to `'"[Gmail]/Sent Mail"'` and the colormap to Blues, we can give the same treatment to our sent email.

#### Image here

<br>
## Step 3: Go further
### most frequently contacted people
### monthly distinct recipients




TODO
* fix email
* fix share buttons (where'd they go!?)
* figure out if publishing an edit triggers rss

