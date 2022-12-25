# Augmented Bonding Curves (ABCs)

`Experimental` 

### Description

An augmented bonding curve (ABC) is a type of smart contract that can be used to fund the development and maintenance of public goods. It is a hybrid of a [bonding curve](https://medium.com/@simondlr/tokens-2-0-curved-token-bonding-in-curation-markets-1764a2e0bee5) and a crowdfunding campaign, in which users can buy tokens that represent a claim on the value of the public good being funded. 

The price of the tokens is determined by an exponential formula that only takes into account the supply of tokens. While creating an algorithm that has price automatically go up with supply may sound like a pyramid scheme, the price only goes up if the demand (supply) for the token actually goes up. If users sell/burn their tokens, then the token's price will come back down just as fast.

In this way, ABCs can be thought of as single-sided markets. The bonding formula determines the price for any given transaction. It doesn't require a counterparty on the other side of the transaction. This property makes it possible to kickstart a small marketplace that might traditionally be illiquid market because it doesn't have enough demand.

Unlike a typical bonding curve system, where tokens can be burned at any point in time, an ABC introduces further mechanisms that lock and vest a share of tokens at the time the pool is created. This vesting period combats any harmful early speculation/arbitrage that would affect the stability of the token pool.

### Examples

- [Commons Stack](https://commonsstack.org/) and their [implementation resources](https://github.com/commons-stack/awesome-bonding)
- [Aragon Fundraising](https://blog.aragon.org/introducing-aragon-fundraising/)

### Further reading

- [Commons Stack: Intro to the ABC](https://commonsstack.org/abc)
- [Deep Dive: Augmented Bonding Curves](https://medium.com/commonsstack/deep-dive-augmented-bonding-curves-b5ca4fad4436)
- [Tokens 2.0: Curved Token Bonding in Curation Markets](https://medium.com/@simondlr/tokens-2-0-curved-token-bonding-in-curation-markets-1764a2e0bee5)
- [LinumLabs: Bonding Curves - The What, Why, and Shapes Behind Them](https://www.linumlabs.com/articles/bonding-curves-the-what-why-and-shapes-behind-it)

### Acknowledgements

- Research and writing by Abbey Titcomb and Commons Stack
- Griff Green described ABCs on the [Greenpill Episode on coordination mechanisms](https://greenpill.substack.com/p/65-coordination-mechanisms-with-griff) as an innovation that is "going to win a Nobel Prize in economics one day"
- ChatGPT: "Can you describe an Augmented Bonding Curve and give two examples of organizations that are using them to fund public goods?"