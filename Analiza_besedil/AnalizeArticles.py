#####
##Prebere članke jih analizira in zapiše v novo csv datoteko z istim imenom v drug direktorij
#####
import textBlob

title="Menlo Ventures is making its first real bet on crypto as Bitpay raises $40 million"
article='''Venture capital firms over the last year or so have wrestled with how forcefully to lean into investing in startups linked to cryptocurrencies:

Is blockchain technology so consequential that we should reorient our entire investment strategy?
Is it a fad that we can avoid as our competitors get distracted?
Or should we gingerly — maybe even reluctantly — make a few investments just to minimize our downside until it’s clearer whether there is indeed money to be made here?
Now an older-line venture firm — Menlo Ventures — is making its first investment in the world of blockchain, the tech that undergirds virtual currencies. Menlo is part of a new $40 million financing round at Bitpay, a startup that allows merchants to accept and store bitcoin paid by customers.

Not all venture capitalists are excited about businesses that rely on normal people using bitcoin for everyday transactions. Investors and startups increasingly see cryptocurrencies as an asset to be traded like gold, not as something to be used at a shopping mall like a dollar bill. And so several top-tier venture capitalists who invest in crypto told Recode they passed on Bitpay amid concerns about how the company’s business model fits into the trends in the industry.

Bitpay CEO Stephen Pair disputed that the company had any trouble fundraising, saying that it had to “expand” the round from a planned $30 million to the final $40 million total due to high demand.

The company did something unusual during fundraising, too: It announced in December its intention to raise a fundraising round that was not yet closed, unveiling the in-progress $30 million round led by a fund managed by Aquiline Capital Partners. Menlo’s investment is part of the same round.

“We wanted to make sure that anybody who wanted to participate could, and announcing it serves that purpose,” Pair said.

That might not be read as a sign of strength, but Bitpay says that in 2017 it processed more than $1 billion in bitcoin payments. Pair says the company has been profitable for a year and a half and therefore hasn’t needed to raise much money — it last raised about $30 million in 2014.

And even if there are some investors and industry veterans who are pessimistic on bitcoin payments in the United States, cryptocurrencies are potentially quite attractive overseas for buying and selling goods. In countries with a large unbanked population or where currency values gyrate wildly, bitcoin can be a stabler form of payment and make commerce easier, especially for the poor.

So it’s no surprise that Bitpay is thinking about using this money to fuel its international expansion, particularly into Asia. Pair said Bitpay could open an office on the continent this year in either Hong Kong or Singapore. Several of the investors in this round are Asia-based.

But what’s most interesting about this round is what it says about how Menlo, founded in 1976, will deal with this new sphere of startup innovation. Tyler Sosin, who is leading Menlo’s work in crypto, said his firm had been evaluating startups using blockchain for the last 18 months but had yet to find something that they loved.

Sosin said that Menlo feels blockchain will be integral to the future of payments — and that they are attracted to payments platforms because it doesn’t require them to bet on the success of any individual cryptocurrency.

Menlo has yet to participate in an initial coin offering, or ICO, Sosin said, nor has it purchased cryptocurrencies outright with firm dollars. While the fund has been slower to engage than some of its rivals, Sosin insisted that the industry is still evolving and that Menlo was eager to dive more fully into this set of startups.

“It’s early, early days,” he said. “We imagine there will be some very big companies.”'''
sentiment = textBlob.get_txt_sentiment(title);
print("title", sentiment)
sentiment = textBlob.get_txt_sentiment(article);
print("article", sentiment)

