Title: Love and Taxes 
Date: 2017-3-11 16:33
Tags: taxes, money, python, visualization
Category: Blog
Slug: love-and-taxes
Author: Tyler Hartley


*Disclaimer: Yes, this is a blog post about taxes. My wife told me it was a bad idea, but here goes.*

Every single year, I overpay my taxes. No matter how many times I adjust my W-4 or sit down with Excel and some pay stubs, I get a big fat refund in the spring. Which, I suppose, can feel nice, until you realize that was your money all along.

So when I got married, I figured I'd finally get this all sorted out. Initially, I assumed that all married couples automatically cut their tax bill. But if that was true, what was this "married filing separately" category all about? For couples that didn't love each other anymore? Unfortunately, it isn't that simple. 

In short, **marriage saves most people thousands a year...but it depends**. Let me explain.

## Tax Math (briefly)

The basics of the Federal Tax system are pretty simple: the more money you make, the higher tax rate you pay. It's called a ["progressive" tax](http://www.investopedia.com/terms/p/progressivetax.asp). A simplified version looks like this:

```
Every dollar between $0 and $10 gets taxed at 10% (so $1)
Every dollar between $10 and $20 gets taxed at 20% (so $2)
Every dollar between $20 and $30 gets taxed at 30% (so $3)
```

If I made $30 in income, I will get taxed $1 + $2 + $3, or $6.[ref]Something that bugs me - people say "I got a raise, now I'm in the 25% bracket which sucks". That misses the point - just the fraction of your income over that bracket gets taxed at that rate. In our simplified example, my tax rate isn't the full 30% rate - only the last $10 I make gets taxed that way. Instead, my actual tax rate is $6 / $30 or 20%.[/ref] But of course, those aren't the real cutoffs - the 2017 Federal Tax Bracket is as follows:

<table class="table">
    <thead>
        <tr>
            <td>Rate</td>
            <td>Single</td>
            <td>Married</td>
            <td>Ratio</td>
        </tr>        
    </thead>
    <tbody>
        <tr>
            <td>10%</td>
            <td>$0 - $9,325</td>
            <td>$0- $18,650</td>
            <td>2.0</td>
        </tr>        
        <tr>
            <td>15%</td>
            <td>$37,950</td>
            <td>$75,900</td>
            <td>2.0</td>
        </tr>        
        <tr>
            <td>25%</td>
            <td>$91,900</td>
            <td>$153,100</td>
            <td>1.7</td>
        </tr>        
        <tr>
            <td>28%</td>
            <td>$191,650</td>
            <td>$233,350</td>
            <td>1.2</td>
        </tr>        
        <tr>
            <td>33%</td>
            <td>$416,700</td>
            <td>$416,700</td>
            <td>1.0</td>
        </tr>        
        <tr>
            <td>35%</td>
            <td>$418,400</td>
            <td>$470,700</td>
            <td>1.1</td>
        </tr>  
        <tr>
            <td>39.6%</td>
            <td>> $418,400</td>
            <td>> $470,700</td>
            <td>~1</td>
        </tr>  
    </tbody>
</table>


## When does marriage save you money?

So two working people get married. They now have a choice: continue to file separately, or combine income and file as married. Is there much of a difference? 

Our first indication that things aren't going to be the same is that the marriage tax brackets aren't simply double the single tax brackets. In the table above, the "ratio" column shows that after 15%, married tax brackets quickly stop being 2x the single ones.

A quick line graph of these tax brackets shows what this divergence looks like:

<img src='/images/taxes/tax_brackets.png' width='500px' alt='Heatmap of taxes saved'/>

The difference between the blue and the red line is the increased taxes a married couple *with identical incomes* would make if they filed jointly vs separately. But the divergence doesn't start until $153k combined salary, which the US Census says is [more than what 90% of households make](https://www.census.gov/library/visualizations/2015/demo/distribution-of-household-income--2014.html).[ref]And we aren't even taking deductions into account yet.[/ref] And below that, the rates are exactly identical &mdash; precisely 2x &mdash; there's no difference between being single or getting married if you make less than $153k.

So given what we know so far, we could conclude that marriage couldn't ever save you on taxes, and would only cost the top 10% of households money. 

### But what if a couple makes vastly different sums of money?

So far in our analysis, we've assumed both spouses make the same salary. Well, here's where things get interesting. Let's look at all possible combinations of spouse income from $0 per year to $200k.[ref]Making sure to take into account a standard deduction and personal exemption. And also assuming no kids. Kids are complicated.[/ref] 

<img src='/images/taxes/heatmap.png' width='100%' alt='Heatmap of taxes saved'/>

Blue areas indicate that this income combination *saves* you money if you get married. Red means a couple would actually pay *more* in taxes by getting married. What's up?

You probably already figured it out by now, but filing jointly means you get to pool your income. So a higher earner gets to effectively "hand off" the highest bits of their income to the other spouse, where that money gets taxed at a lower rate! Two examples:

**Couple A**

* Spouse 1: $50k/year
* Spouse 2: $50k/year

**Couple B**

* Spouse 1: $100k/year
* Spouse 2: $0

Couple A falls precisely into the giant white area of the graph. As in, literally a $0 difference between being married and unmarried. We already knew this from the first graph.

But Couple B, though their combined income is the same as Couple A, fall into the dark blue area of the graph &mdash; they save big bucks. In fact, **the government will cut their tax bill by $6,861 for getting married!**[ref]Now, to be clear - both Couple A and Couple B pay *the exact same amount in taxes*. It's not that Couple B pays less &mdash; it's that the difference between them being unmarried and married is huge.[/ref] 

To actually lose money getting married (it's called the "Marriage Penalty"), both spouses need to be earners and both need to be making ~$90,000 or more. The penalty starts off small at first, only $1,000 or so, and then quickly baloons into the dark red area. It is for these types of couples that "married, filing separately" exists.[ref]#WealthyCoupleProblems.[/ref]

## Incentives

The Couple A vs Couple B example raises some interesting questions. What is the federal government trying to incentivize with this tax structure? 

**Our tax code encourages families with one primary breadwinner over families with two incomes.** Put differently, you could argue it's encouraging stay-at-home parents. Almost like a credit for one parent leaving the workforce (or earning dramatically less). Without taking sides on that particular issue, it's worth noting that the single-earner household is [no longer the most common  type of household and hasn't been for 35 years](http://www.pewresearch.org/ft_dual-income-households-1960-2012-2/). In 60% of families, both spouses work.

On the other side of the coin, the tax code penalizes wealthy couples who both earn significant incomes. But given the option to file separately, these couples won't actually be penalized &mdash; they just won't be advantaged, either.

Among certain circles, this is a pretty well-understood connundrum &mdash; and one that's been debated for decades. (I didn't discover this issue. I just made a pretty graph about it.) Reading deeper about it gets pretty political pretty quick, but there are some interesting takeaways. You could ensure *all* married couples get a tax incentive regardless of income by removing the married tax bracket altogether and giving spouses a flat or fractional tax deduction. This is pretty much how the child tax credit works. Or you could eliminate the "marriage penalty" by simply making the marriage tax brackets twice the single ones.[ref]Which is actually how taxes worked in the US [between '48 and '69](http://www.ctj.org/html/marpen.htm)[/ref] But this isn't at the top of any politicians' radars.

That's because in the end, it's unlikely any of these idiosyncracies in our tax structure are going to actually push a couple to get married or avoid marriage[ref]Can you imagine what an awkward proposal that would be? "With this ring, will you save me $6,861 annually?"[/ref]. But I think we can at least agree the federal tax code has a somewhat...outdated view of marriage.

*You may now stop thinking about taxes. I am sorry.*

