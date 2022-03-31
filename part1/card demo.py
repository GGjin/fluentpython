import collections
from random import choice

Card = collections.namedtuple("Card", ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


beer_card = Card('7', 'diamonds')
# print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])
print(choice(deck))
# 查看最上面三张
print(deck[:3])
# 先抽出索引12的牌，然后每隔13张牌拿一张， 就是只看牌面是A的牌的操作
print(deck[12::13])
# for card in deck:
#     print(card)
print(Card('Q', 'hearts') in deck)
print(Card('7', 'bearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
