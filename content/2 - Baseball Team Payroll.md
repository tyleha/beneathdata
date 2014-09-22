Title: Does money buy wins in Baseball?
Date: 2014-9-04 10:20
Tags: baseball, python, statistics, money
Category: Blog
Slug: money-in-baseball
Author: Tyler Hartley
<!-- Summary: Short version for index and feeds -->

Since _Moneyball_ was published in 2003, the idea that money is as much a part of the game as first basemen or the infield grass has become common knowledge. We all understand the basic notion that in Major League Baseball, money can define who plays on your team and therefore _how_ your team plays. What _Moneyball_ wanted to convey is that even still, money isn't everything. What the book didn't ask is "ok, money isn't everything, but how much is it worth?"

I have been curious about how money affects my favorite sport since the _Moneyball_ days. I grew up watching the Atlanta Braves, owned by wild-eyed tycoon Ted Turner. In the '90s, Turner was happy to shell out money for the Braves, so long as it produced wins. As we'll see later, it sure did. However, after the team was aquired by a cheaper ownership group in 2007, the kinds of players we could afford and the kind of team we fielded suddenly changed. But our success (generally) continued. How? It seems intuitive that teams with deep pockets can buy the best players and thus put together the best teams. But we see time and time again that small-market teams with smaller payrolls still manage to compete in baseball...don't we? Conventional wisdom seems to point in both directions - the Yankees buy great players and field great teams, but the A's and the Rays have tiny salaries and great histories of success. Who's right? 

Various sources have tried to tackle this question in variously incompelte ways. Wikipedia notes that "_...the New York Yankees have consistently had the highest total payroll in MLB, and they have appeared in 40 of the 109 World Series for 27 wins as of 2013 (36.7% of all World Series for a 24.8% success rate)._" [[1]](http://en.wikipedia.org/wiki/Salary_cap#Major_League_Baseball_.28luxury_tax.29) That's great, but the Yankees are one example. Somebody at Columbia Business School did a deeper investigation of the idea and concluded that 20% of success in baseball can be attributed to payroll [[2]](http://www.sloansportsconference.com/wp-content/uploads/2014/02/2014_SSAC_Why-money-is-not-baseballs-most-valuable-currency.pdf). Better. But how have rich teams fared compared to poor teams? How does money affect the playoffs, if at all? 

Baseball stands apart from other North American sports in that it doesn't have a salary cap. It is this single fact that makes this debate possible - teams can spend whatever they want! In the NFL or NBA, money can't logically have a powerful effect on wins; each team has the same chips to play with. But baseball has never operated this way. I think it's worth a look back (real quick I promise!) to understand how we ended up here.

#### A brief history of Baseball salaries
When baseball began, teams _owned_ players. And I mean owned. Players either played for the team that controlled their rights, or they didn't play baseball at all. Free agency didn't exist - trades were the only time a player switched uniforms. Salaries were relatively consistent across teams because intra-team collusion could hold player salaries down.

Then came the 1970's. Players banded together and negotiated Free Agency. FA meant that a player could enter the open market and sell his talents to the highest bidder, which opened the floodgates for spending in baseball. Suddenly, the artifically low salaries players were making in the early '70s skyrocketed (if this stuff floats your boat, go check out a great history of the economics of baseball [here](http://eh.net/encyclopedia/the-economic-history-of-major-league-baseball/)). Rich teams could simply outbid their opponents for a free agent while the poorer teams had to find alternate means. This is a great point to dive into the data.

#### The base data
I collected information on team history from the great [baseball-reference.com](http://baseball-reference.com) and cobbled together team salaries from a few wonky resources. Salary data hasn't always been available. Nearly nothing is out there from before 1977 though, since 1985, team salaries have been [public record](http://sabr.org/research/mlbs-annual-salary-leaders-1874-2012). So the data set we'll have to work with covers 1977 to 2013, with high confidence in the data post '85. 

The first thing I noticed is the incredible growth of player salaries in baseball. Take a look at the chart below. Since 1977, salaries have increased a whopping 71 times over (unadjusted for inflation). If somehow you were able to invest $10k in an index fund of baseball salaries 40 years ago, it would now be worth nearly three-quarters of a million dollars. By contrast, the median US income has only increased 4x and the entire NASDAQ (which barely existed in 1977) only 45x. 

Because of this massive growth in player salaries, we can't compare team salaries across the years. Even adjusting for inflation won't do us any good. Instead, I tried to come up with a relative metric that would be fair to compare payrolls in 1980 to payrolls from 2013. I chose [Median Absolute Deviations (MAD)](https://dipot.ulb.ac.be/dspace/bitstream/2013/139499/1/Leys_MAD_final-libre.pdf), which you can think of as just standard deviations but less sensitive to outliers (_ahem_ Yankees _ahem_). 

## Team Wins vs Team Payroll
Using MADs, we can compare each team to the median salary that year and figure out how far above or below that median value they were. If we compare MADs to wins, we can get a feel for how outspending your opponents helps your team's win total for that year. Take a look below:

![Alt text](/path/to/img.jpg)

The linear regression line there clearly indicates that the data has a positive bias, with a slope of 3.8. That means that for every standard deviation you outspend the rest of the league, you can (on average) expect a 4 win boost. The inverse is also true. But the correlation to this line is terrible. Teams are all over the map both above and below this line. That's not surprising - there's a lot that makes a team on the field good other than just how much the players cost. And that's not even taking into account the inherent randomness in baseball. This plot really just gives us an idea, but it does hint that underneath it all money _does_ help teams win more games. 

I read a good argument pointing out that if you want to find a relationship between money and wins, you need to look long term. This makes intuitive sense - it takes a baseball team years to build up farm system, get the right free agents, and gel a team together. So instead, let's look at average yearly wins over roughly 10-year spans vs payroll.

![Alt text](/path/to/img.jpg)

Now we've got a nicer looking linear relationship. 
A few notes:

+ The Yankees are far and away the highest spending team from decade to decade. But since the early 2000's, they've been outspending opponents like no team ever before.


You can download my data here if you'd like to fiddle around with it yourself.

