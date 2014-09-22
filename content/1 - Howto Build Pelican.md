Title: How I Built this Website using Pelican
Date: 2014-9-22 11:15
Tags: how-to, python, pelican, website
Category: How To
Slug: how-i-built-this-website
Author: Tyler Hartley

I have wanted to run a data blog for a good long while now. And, like any aspiring blogger, I had various failed attempts that never got off the ground. Half the reason was that, well, writing is hard. The other half of the reason is that I can be a ridiculous control freak when it comes to digital design. 

I tried __Weebly__ (they let me use a custom domain for free), but the interface was clunky and the UI always looked cookie-cutter.

I tried __Wordpress__, but I couldn't get fine-grained enough control of the HTML/CSS without forking over the $100+ annual Pro fee.

I even looked at __Squarespace__, which nearly had me convinced (those are some beautiful templates over there), but frankly, it's just too Web 2.0 for me. Though if I was a photographer or an [artisinal lightbulb maker](http://www.imdb.com/video/imdb/vi3729299993), I'd use Squarespace in a heartbeat.  

To top it all off, I kept feeling ashamed, like I know enough programming that I should just do it myself. But I didn't want to start from scratch or even from medium scratch like Django. That's where Pelican came in. 

![]()

## What is Pelican?
Pelican is a static-site generation tool that abstracts a massive amount of the HTML/CSS generation for you, and lets you write your post in Markdown or RST or whatever markup your little heart desires. It has a rich community offering dozens of cool plugins and custom-built themes, all simple to edit to your tastes, right down to the raw HTML, CSS, and JS. To top it all off, because Pelican creates static sites, you can host your website for _absolutely free_ on Github Pages or for pennies a month on Amazon S3 (more on that later). No server maintenance, no hosting fees, no fuss.

For an occasional perfectionist like me, Pelican was a godsend. I quickly was able to get a good-looking, mobile-ready site up and running and, of course, add _content_. If you too are interested in building your own custom website (for free!), then follow along. Feel free to post questions in the comments.

## Setting up your environment

First off, Pelican is well documented. Read the docs [here](http://docs.getpelican.com/en/latest/quickstart.html) - they are great.

Things you'll need to run Pelican
* Python
* Pelican
* Markdown (if that's your thing)
* Fabric, probably, for automation

Woo! That's it. Assuming you have Python 2.7.x or 3.3.x, just run the following:

```bash
pip install pelican markdown
```

## Quickstart
Fist things first - use pelican's quickstart method to build the default website. We'll get around to applying themes in a bit. Use the `pelican-quickstart` command and follow the prompts

```bash
>pelican-quickstart

Welcome to pelican-quickstart v3.4.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

> Where do you want to create your new web site? [.] folder_to_use
> What will be the title of this web site? BlogName
> Who will be the author of this web site? Your Name
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) y
> What is your URL prefix? (see above example; no trailing slash) http://mycustomdomain.com
> Do you want to enable article pagination? (Y/n) y
> How many articles per page do you want? [10]
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) y
> What is the name of your S3 bucket? [my_s3_bucket]
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at home/tyler/folder_to_use
```

Note that all these settings can be modified later - you're not locked into anything, but Pelican's trying to make it easy on you.

I'm not going to go into detail about how to create posts or modify additional Pelican settings, because they're entirely up to your tastes and are extensively documented in [Pelican's Docs](http://docs.getpelican.com/en/latest/quickstart.html).

You're now ready to fire up Pelican, locally at least. All you need to do is one of the following, depending on your OS and preferences

1. `fab build` followed by `fab serve` (or just `fab reserve`)
2. `make html` and then `make serve`
3. `pelican content -s publishconf.py` followed by `cd output`, `python -m SimpleHTTPServer`

Boom. You're up and running on localhost:8000.

## Applying a theme

Ok, so the default Pelican theme looks sort of like Pepto Bismol. We can fix that! Check out the list of existing Pelican themes over at https://github.com/getpelican/pelican-themes. Having looked at screenshots of them all, my favorites are (in order):

1. [pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3) - The theme this website uses, which leverages the massively popular Bootstrap library and Bootswatch themes. 
2. [html5-dopetrope](https://github.com/PierrePaul/html5-dopetrope)
3. [pure](https://github.com/PurePelicanTheme/pure)

To apply a theme, it's this easy - get yourself a copy of the repo, stick it somewhere (maybe in your project folder, up to you), and then point Pelican to it in your pelicanconf.py script with the variable 

```python
THEME = '/path/to/theme'
```

It is THAT easy. 

Of course, you can now go nuts and modify the theme however you like. Pelican-bootstrap3's features are [well documented](https://github.com/DandyDev/pelican-bootstrap3/blob/master/README.md). For what it's worth, if you'd like to use my precise custom theme, clone it from my repo [here](). You can check out my pelicanconf.py settings [here](https://github.com/tylerhartley/thedatashow/blob/master/pelicanconf.py).

## Publishing to Github Pages

First you'll need to decide if you want to use a Github user page or project page. The difference here is not trivial. The user page is served at yourgithubname.github.io, while the projects are served at yourgithubname.github.io. Of course, we'll end up mapping those urls to other registered custom domains, and the majority of you will want to use an apex domain (e.g. mywebsite.com, not blog.mywebsite.com). Unfortunately on Github Pages, a mapped apex domain will be 

## Publishing to Amazon S3