Title: Does money buy wins in Baseball?
Date: 2014-9-04 10:20
Tags: baseball, python, statistics, money
Category: Blog
Slug: money-in-baseball
Author: Tyler Hartley
<!-- Summary: Short version for index and feeds -->

Since _Moneyball_ was published in 2003, the idea that money is as much a part of the game as first basemen or the infield grass has become common knowledge. We all understand the basic notion that in Major League Baseball, money can define who plays on your team and therefore _how_ your team plays. Basically, the story goes like this - big, behemoth teams like the New York Yankees can buy their way to a championship. But the little guys, they have to pick out the diamonds in the rough and put together a ragtag team utilizing advanced metrics. What _Moneyball_ wanted to convey is that even if money is limitless in baseball, money isn't everything. What the book didn't ask, however, is "ok, money isn't everything, but how much is it worth?"

## Conventional Wisdom

It seems intuitive that teams with deep pockets can buy the best players and thus put together the best teams. But we see time and time again that small-market teams with smaller payrolls still manage to compete in baseball...the Oakland Athletics, the Tampa Bay Rays... But simultaneously, we see the Yankees dominate for two decades, we see the Red Sox come to power in the '00's on a rising payroll we see the 2013 Dodgers spend (and win) like there's no tomorrow. Conventional wisdom seems to point in both directions. Who's right? 

Various sources have tried to tackle this question in variously incomplete ways. Wikipedia notes that "_...the New York Yankees have consistently had the highest total payroll in MLB, and they have appeared in 40 of the 109 World Series for 27 wins as of 2013 (36.7% of all World Series for a 24.8% success rate)._" {[1](http://en.wikipedia.org/wiki/Salary_cap#Major_League_Baseball_.28luxury_tax.29)} That's great, but the Yankees are an anecdote. Somebody at Columbia Business School did a deeper investigation of the idea and concluded that 20% of success in baseball can be attributed to payroll {[2](http://www.sloansportsconference.com/wp-content/uploads/2014/02/2014_SSAC_Why-money-is-not-baseballs-most-valuable-currency.pdf)}. Better. But what causes this effect? And how has this trend evolved over time? 

## A brief history of Baseball salaries

Baseball stands apart from other North American sports in that it doesn't have a salary cap - teams can spend whatever they want! In the NFL or NBA, money can't logically have a powerful effect on wins; each team has the same chips to play with. But baseball has never operated this way. I think it's worth a look back (real quick I promise!) to understand how we ended up here.

When baseball began, teams _owned_ players. And I mean owned. Players either played for the team that controlled their rights, or they didn't play baseball at _all_. Free agency didn't exist. Trades were the only time a player switched uniforms. Salaries were relatively consistent across teams because intra-team collusion held player salaries down.

Then came the 1970's. Players banded together and negotiated Free Agency. FA meant that a player could enter the open market and sell his talents to the highest bidder which opened the floodgates for spending in baseball. Now rich teams could simply outbid their opponents for a free agent while poorer teams had to find alternate means. Suddenly, artificially low player salaries skyrocketed as the market equalized {if this stuff floats your boat, go check out a great history of the economics of baseball [here](http://eh.net/encyclopedia/the-economic-history-of-major-league-baseball/)}. 

We can actually witness this equalization happening, as salary data since 1977 is publicly available and I cobbled it together from a few sources. {footnote: I collected information on team history from the great [baseball-reference.com](http://baseball-reference.com) and cobbled together team salaries from a few wonky resources. Salary data hasn't always been available. Nearly nothing is out there from before 1977 though, since 1985, team salaries have been [public record](http://sabr.org/research/mlbs-annual-salary-leaders-1874-2012). So the data set we'll have to work with covers 1977 to 2013, with high confidence in the data post '85.} 

![The axes aren't right to see it, but good god textbook prices have risen!](/images/baseball/Total_Salary.png)

Since 1977, MLB salaries have increased a whopping 71 times over (unadjusted for inflation). If somehow you were able to invest $10k in an index fund of baseball salaries 40 years ago, it would now be worth nearly three-quarters of a million dollars. By contrast, the median US income has only increased 4x and the entire NASDAQ (which barely existed in 1977) "only" 45x. 

## Team Wins vs Team Payroll

Because of this **massive** growth in player salaries, we can't simply compare team salary dollar values across the years. So, I utilized a metric to normalize payrolls called [Median Absolute Deviations (MAD)](https://dipot.ulb.ac.be/dspace/bitstream/2013/139499/1/Leys_MAD_final-libre.pdf). You can think of MAD as just standard deviations from the mean, but less sensitive to outliers (_ahem_ Yankees _ahem_). If you don't know what a standard deviation is, just think of MADs as money.

#### Effect of Money All-Time
Now, we can compare salaries of teams from 1976 to 2013. Let’s just take the dummy approach – plot the wins vs MAD salary of every single team since 1977.

![All time correlation between wins and salary](/images/baseball/Wins_vs_salary_all_teams_all_time.png)

There’s a positive relationship there, 3.8 wins predicted for every stdev you outspend the league, but it’s not strong. We can say "sure, money has a nonzero effect on Baseball," but there’s a lot of noise. Is this noise because of the inherent randomness in a baseball season, or is it because money has a really weak effect on winning? Both?

Let's break that graph down into roughly 10 year periods. 

![Decade-by-decade correlation between wins and salary](/images/baseball/Salary_vs_Wins_by_decade.png)

We see basically the same thing as in the previous graph, except now it’s amusing to look at the A’s vs the Yankees post-1993 {FOOTNOTE: notice the A’s in the 80’s and early 90’s – their heyday. They won the world series, they had incredible stars like Dennis Eckersley, they were on top. It’s also the only time in their history they won the world series. Now look at the years since 1994 – their payroll has been consistenly in the bottom half and yet they’ve been winning pretty above the best fit line. This is proof that at least part of Moneyball’s thesis is true – smart teams like the A’s can outperform their salaries. On the other hand, look at the Yankees. Nearly always waaaay out to the right. Nearly always winning. They set the trend. They are the reason for the Luxury Tax.}. 

#### Effect of Money Long-Term
Let’s adjust our hypotheses – it’s not JUST money that wins baseball games. More specifically, it’s money applied over time. Below you’ll see the same graph as before, just with each team averaged into a single data point. 

![Alt text](/images/baseball/salary_avg_by_decade.png)

The slopes of each line have increased and the R values have increased considerably. We might reasonably conclude that increased payroll, when kept high over time, has a significant effect on the performance of the team, in the neighborhood of 5 wins per MAD (standard deviation), meaning you could expect a team like the Yankees to consistently win 10 more games than league average, or 91 games. 91 games pretty much assures you a spot in the playoffs nowadays, so yeah, **NOT** insignificant.These results make intuitive sense - it takes a baseball team years to build up farm system, get the right free agents, and gel a team together.



## The Competitive Balance and MLB Luxury Tax

Interestingly, the magnitude of the effect of money on baseball success has changed over the decades, peaking in the ’94-’03 era. Honestly, if you’d put a gun to my head and made me guess what 10-year period would show the most powerful monetary effects, I would have guessed pretty much these 10 years. Here’s why. Money has some stuff to do with your owners, but even MORE to do with your revenue team. If you’re a big market team, sure you’ll get better attendance and more merchandise purchased. But beginning in 1990, baseball saw the first truly, insanely lucrative TV deals being to pop up. It began with ____ ___ and progressed from there. With their newfound cash prospects, some teams were suddenly able to outspend their opponents by ridiculous margins. 








Of course, dropping money one offseason in baseball doesn't necessarily pay dividends immediately - you still have to find the right free agents, develop a few prospects, and gel a team together. 



![Alt text](/images/baseball/salary_avg_by_decade.png)

Note that the slopes have increased slightly and the R values have increased considerably. We can say with some confidence that baseball teams who outspend their opponents in the long run are more likely to win, somewhere in the neighborhood of 5 wins per standard deviation. 5 wins is _not_ insignificant. In fact, we can say that in the pe

A few additional notes:

* The power of money in baseball
* The Yankees are far and away the highest spending team from decade to decade. But since the early 2000's, they've been outspending opponents like no team ever before.

We can more easily see the 

## 


Scratch
===========================


You can download my data here if you'd like to fiddle around with it yourself.

