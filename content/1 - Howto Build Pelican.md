Title: How I built this website using Pelican
Date: 2014-9-22 11:15
Tags: how-to, python, pelican, website
Category: How To
Slug: how-i-built-this-website
Author: Tyler Hartley

I have wanted to run a data blog for a good long while now. And, like any aspiring blogger, I had various failed attempts that never got off the ground. Half the reason was that, well, writing is hard. The other half of the reason is that I can be a ridiculous control freak when it comes to digital design. 

I tried __Weebly__ (they let me use a custom domain for free), but the interface was clunky and the UI always looked cookie-cutter.

I tried __Wordpress__, but I couldn't get fine-grained enough control of the HTML/CSS without forking over the $100+ annual Pro fee.

I even looked at __Squarespace__, which nearly had me convinced (those are some beautiful templates over there), but frankly, it's just too Web 2.0 for me. Though if I was a photographer or an [artisanal light bulb maker](http://www.imdb.com/video/imdb/vi3729299993), I'd use Squarespace in a heartbeat.  

To top it all off, I kept feeling ashamed, like I know enough programming that I should just do it myself. But I didn't want to start from scratch or even from medium scratch like Django. That's where Pelican came in. 

![The Pelican](https://avatars0.githubusercontent.com/u/2043492?v=2&s=200)

## What is Pelican?
Pelican is a static-site generation tool that abstracts a massive amount of the HTML/CSS generation for you, and lets you write your post in Markdown or reST or whatever markup your little heart desires. It has a rich community offering dozens of cool plugins and custom-built themes, all simple to edit to your tastes, right down to the raw HTML, CSS, and JS. [If you've heard of Jekyll before, it's that, but written in Python.] 

To top it all off, because Pelican creates static sites, you can host your website for *__absolutely free__* on Github Pages or for pennies a month on Amazon S3 (more on that later). No server maintenance, no hosting fees, no fuss.

For an occasional perfectionist like me, Pelican was a godsend. I quickly was able to get a good-looking, mobile-ready site up and running and, of course, add _content_ with ease. If you too are interested in building your own custom website (for free!), then follow along. Feel free to post questions in the comments.

## Setting up your environment

First off, Pelican is well documented. Read the docs [here](http://docs.getpelican.com/en/latest/quickstart.html) - they are great.

Things you'll need to run Pelican

* Python
* Pelican
* Markdown (if that's your thing)
* Fabric, probably, for automation

Woo! That's it. Assuming you have Python 2.7.x or 3.3.x, just run the following:

```bash
$ pip install pelican markdown fabric
```

## Quickstart
First things first - use pelican's quickstart method to build the default website. We'll get around to applying themes in a bit. Use the `pelican-quickstart` command and follow the prompts

```bash
$ pelican-quickstart

Welcome to pelican-quickstart v3.4.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.

$ Where do you want to create your new web site? [.] folder_to_use
$ What will be the title of this web site? BlogName
$ Who will be the author of this web site? Your Name
$ What will be the default language of this web site? [en]
$ Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) y
$ What is your URL prefix? (see above example; no trailing slash) http://mycustomdomain.com
$ Do you want to enable article pagination? (Y/n) y
$ How many articles per page do you want? [10]
$ Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
$ Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
$ Do you want to upload your website using FTP? (y/N) n
$ Do you want to upload your website using SSH? (y/N) n
$ Do you want to upload your website using Dropbox? (y/N) n
$ Do you want to upload your website using S3? (y/N) y
$ What is the name of your S3 bucket? [my_s3_bucket]
$ Do you want to upload your website using Rackspace Cloud Files? (y/N) n
$ Do you want to upload your website using GitHub Pages? (y/N) y
$ Is this your personal page (username.github.io)? (y/N) y
Done. Your new project is available at home/tyler/folder_to_use
```

Note that all these settings can be modified later - you're not locked into anything, but Pelican's trying to make it easy on you.

I'm not going to go into detail about how to create posts or modify additional Pelican settings, because they're entirely up to your tastes and are extensively documented in [Pelican's Docs](http://docs.getpelican.com/en/latest/quickstart.html).

You're now ready to fire up Pelican, locally at least. All you need to do is one of the following, depending on your OS and preferences

1. `fab build` followed by `fab serve` (or just `fab reserve` to do both at once)
2. `make html` and then `make serve`
3. `pelican content -s publishconf.py` followed by `cd output`, `python -m SimpleHTTPServer` (ugh...just install fabric and do #1)

Boom. You're up and running on **localhost:8000**.

## Applying a theme

Ok, so the default Pelican theme looks sort of like Pepto Bismol. We can fix that! Check out the list of existing Pelican themes over at [https://github.com/getpelican/pelican-themes](https://github.com/getpelican/pelican-themes). Having looked at all the available themes, my favorites are (in order):

1. [pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3) - The theme this website uses, leveraging the massively popular Bootstrap library.
2. [html5-dopetrope](https://github.com/PierrePaul/html5-dopetrope)
3. [pure](https://github.com/PurePelicanTheme/pure)

with `pelican-bootstrap3` being far and away my favorite and best documented. To apply a theme, it's this easy - get yourself a copy of the repo, stick it somewhere (maybe in your project folder), and then point Pelican to it in your pelicanconf.py script with the setting:

```python
THEME = '/path/to/theme'
```

It is **THAT** easy. 

Of course, you can now go nuts and modify the theme however you like. Pelican-bootstrap3's features are [well documented](https://github.com/DandyDev/pelican-bootstrap3/blob/master/README.md). With relatively little effort, I added a banner image, a custom footer, and tweaked stylings. Pelican leverages a Django-like template format and Jinja2, which means that editing site-wide content requires editing only a single file. For what it's worth, if you'd like to use my precise custom pelican-bootstrap3 theme, you can clone it from my repo [here](https://github.com/tylerhartley/pelican-bootstrap3). You can also see my precise pelicanconf.py settings as a guide [here](https://github.com/tylerhartley/beneathdata/blob/master/pelicanconf.py).

## Where you gonna host this thing?

First you'll need to decide where you want to host your site. Sure, you could do it on a Heroku server and whatnot, but remember this is a static site! It can be served anywhere that serves flat files!![ref]even Dropbox...![/ref] 

The two most popular options are probably Github Pages and Amazon S3. The features are nearly identical and the cost is either nil or a couple quarters/mo. But, the one discriminating fact that led me to Amazon S3 has to do with website speed. 

When this is all said and done, you probably want to access your Pelican site from an apex domain like **beneathdata.com**. It's the norm. Unfortunately on Github Pages, a mapped apex domain will be [_really_. _slow_](http://instantclick.io/github-pages-and-apex-domains). However, if you map a custom subdomain like **blog.beneathdata.com**, Github will serve your static site plenty fast. The underlying reason has to do with A/ALIAS records, CDNs, and other fancy stuff, but there's the rub. YES, you could get around the problem on Github Pages with a custom CDN like CloudFlare. But if you want fine-grained control over your CDN, you'll have to look elsewhere.

Amazon S3 fills that nice nicely, and serves an apex domain by routing traffic through their Route 53 DNS service for $0.50/month, which can then be hooked into Amazon's CloudFront CDN. Choose wisely. Both options will get you a great site.  

## Github Pages

First you'll need to decide if you want to use a Github user page or project page. The only real difference is default Github url - username.github.io for user pages and username.github.io/projectname for projects.  

To get started with GH Pages, follow the instructions [here](https://pages.github.com/). Once you have your repo created, clone it and create a branch. I called mine source. 

```bash
$ git branch -b source
```

Here's where you're going to put all your pelican files. Your content folder, your theme folder, the pelicanconf.py file, everything needed to build your site. When you're ready to push your Pelican site live, you'll need **[ghp-import](https://github.com/davisp/ghp-import)**. 

`ghp-import` allows us to copy the contents of a specific folder to a separate git branch. Saves a ton of time, and makes updating your Github Pages site a two-command action.

Github will only look in a specific branch for the HTML content to serve your static site - the `master` branch for user pages and the `gh-pages` branch for projects. So, depending on which page you're using, run the following command from your `source` branch:

```bash
$ ghp-import -m 'commit message' -b master output
$ git push --all
```

**Boom. Your site is now live.** Isn't that awesome? Replace master with gh-pages and output with wherever your output HTML goes as necessary.

Alternatively, you could make a Fabric command to do this all in one move, and maybe commit your current branch at the same time, like the following:

```python
def publishghp(msg):
    preview() #builds publishconf.py
    local("git add -A") #will commit allll files, be careful
    local("git commit -m '%s'"%msg)
    local("ghp-import -m '%s' -b master output"%msg)
    local("git push --all")
```

You can then commit and push in one line, passing the commit message to the fabric command like so:

```bash
$ fab publishghp:"commit message"
```

Happy blogging.

## Amazon S3
If you, like me, want to use an apex domain with Pelican, or you're just a big Amazon fan, then Amazon S3 is for you. It isn't quite free (maybe $0.75/month for me, so still insanely cheap) and it sure isn't as hip as Github, but it gets the job done. 

Again, follow Amazon's [really outstanding instructions](http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) to get your static site set up, then come back here and we'll talk about pushing to S3.

Like `ghp-import` for Github Pages, the open-source community has gone and done us a solid and created [s3cmd](http://s3tools.org/s3cmd). It's not as easy to use as ghp-import, but you really only need one command. 

`s3cmd` is designed as a full-feature command line manager of your s3 bucket, but all we'll use it for is pushing files up. For that, we'll stick to the `sync` command which tries to only upload files that differ between local and cloud to save bandwidth.

My big complaint about `s3cmd` is its massive inability to correctly figure out file mime-types, which wasn't even a problem I was aware existed in the world until using this program. 

To get around the issue, **make sure** you are using at least **s3cmd v1.5**. Then, upload your website with this command:

```bash
s3cmd sync output/ --acl-public --guess-mime-type s3://bucketname/
```

on UNIX and

```bash
python path\\to\\s3cmd\\s3cmd sync output/ --acl-public --guess-mime-type s3://bucketname/
```

on Windows.[ref]I tested s3cmd on Windows and it _does_ work, it's just annoying. Stick to UNIX.[/ref]] `output/` is the directory we're pushing to S3 with the trailing slash. `--acl-public` guarantees that the files are viewable by anyone (it's a website, dummy) and `--guess-mime-type` does just that. If you're on UNIX, you may need to `apt-get remove python-magic` for it to work. Ugh. But: **Boom. Your site is now live**. 

## Wrap-up

You just made a good-looking website that you're hosting for (essentially) free and have full source control over! Congrats!

Of course, it's all the hard work in between these above commands that are going to make or break your website. Pelican just makes it easy to get down to the actual task of _writing_ your blog, but hopefully this post has made it that much easier still.