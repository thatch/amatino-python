# Amatino Python

Amatino is a double-entry accounting system. It provides double entry accounting as a service via an HTTP API. Amatino Python is a library for interacting with the Amatino API from within a Python application. By using Amatino Python, a Python developer can utilise Amatino services without needing to deal with raw HTTP requests.

## About Amatino

Amatino gives you a full set of tools to store, organise and retrieve financial information. You don't need to set up databases or write any of your own double-entry accounting logic. All you need is this library, an [Amatino account (Try free for two weeks!)](https://amatino.io/subscribe), and you are off and running.

## Under construction

Right now, the Amatino API offers a full range of accounting services via HTTP requests. However, this Amatino Python library is in an 'Alpha' state. Its capabilities are limited. A subset of full Amatino features are available.

To see what proportion of Amatino features are ready in Amatino Python, check out the [Documentation](https://github.com/amatino-code/amatino-python/wiki/Documentation) page. Linked classes are available, un-linked ones are still under construction.

## Installation

Amatino Python may be installed via [PIP](https://pypi.org/project/amatino/).

````bash
$ pip install amatino
````

To use Amatino Python, you will need an active Amatino subscription. You can start a free trial at [https://amatino.io/subscribe](https://amatino.io/subscribe).

## Example Usage

The first step is to login to  Amatino by creating a [Session](https://github.com/amatino-code/amatino-python/wiki/Session) instance. That Session then becomes your key to using Amatino classes.

```python
from amatino import Session

session = Session.create_with_email(
  email='clever@cookie.com',
  secret='uncrackable epic passphrase!'
)
```

Amatino stores financial data inside discrete [Entities](https://github.com/amatino-code/amatino-python/wiki/Entity). An Entity might describe a person, project, company, or some other entity which you wish to describe with financial data.

```python
from amatino import Entity

mega_corporation = Entity.create(
  session=session,  # Created above
  name='Mega Corporation'
)
```

Entities are structured as a hierarchical tree of [Accounts](https://github.com/amatino-code/amatino-python/wiki/Account). You might wish to create a chart of Accounts that mirror the real-world structure of the Entity you are describing.

```python
from amatino import Account

revenue = Account.create(
  entity=mega_corporation,  # Created above
  description='Revenue from world domination',
  am_type=AMType.revenue,  # An AMType enumeration option
  denomination=USD  # A GlobalUnit
)
```

The real fun begins with [Transactions](https://github.com/amatino-code/amatino-python/wiki/Transaction), where debits and credits come into play

```python
from amatino import Transaction, Entry, Side
from datetime import datetime
from decimal import Decimal

revenue_recognition = Transaction.create(
  entity=mega_corporation,
  time=datetime.utcnow(),
  entries=[
    Entry(Side.debit, Decimal(10), cash),
    Entry(Side.credit, Decimal(5), revenue),
    Entry(Side.credit, Decimal(5), customer_deposits)
  ]
  denomination=USD
)
```

Check out the full range of available classes, including Ledgers, in the [Amatino Python documentation](https://github.com/amatino-code/amatino-python/wiki/Documentation)

## API stability & versioning

Amatino Python obeys the [Semantic Version](https://semver.org) convention. Until v1.0.0, the Python API (not to be confused with the Amatino HTTP API) should be considered unstable and liable to change at any time.

>**Watch out! API currently unstable!**

You can see available versions [in GitHub's releases section](https://github.com/amatino-code/amatino-python/releases) or [in PyPi's release history section](https://pypi.org/project/amatino/#history).

## Tell us what your think/want/like/hate

Please join us on the [Amatino discussion forums](https://amatino.io/discussion) and give us your feedback. We would love to hear from you. Amatino is in its earliest stages of development, and your feedback will influence the direction it moves in.

Pull requests, comments, issues, forking, and so on are also [most welcome on Github](https://github.com/amatino-code/amatino-python)!

## Useful links

 - [Amatino home](https://amatino.io)
 - [Development blog](https://amatino.io/blog)
 - [Development newsletter](https://amatino.io/newsletter)
 - [Discussion forum](https://amatino.io/discussion) 
 - [More Amatino client libraries](https://github.com/amatino-code)
 - [HTTP Documentation](https://amatino.io/documentation)
 - [Python Documentation](https://github.com/amatino-code/amatino-python/wiki/Documentation)
 - [Billing and account management](https://amatino.io/billing)
 - [About Amatino Pty Ltd](https://amatino.io/about)

## Get in contact

To quickly speak to a human about Amatino, [email hugh@amatino.io](mailto:hugh@amatino.io) or [yell at him on Twitter (@hugh_jeremy)](https://twitter.com/hugh_jeremy).
