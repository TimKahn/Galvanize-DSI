"""
Matthew Drury's Probabilty Problem:

You have a shuffled deck of 60 cards containing the following cards of special interest:
- Three of the cards in the deck are marked with a diamond.
- Three of the cards are marked with a star.
- The remaining cards are nothing special.

You draw an initial hand of five cards, after which you *must* discard any of
the star cards for an additional three cards drawn from the top of the deck.
This process is repeated until you find yourself with a hand that does *not*
contain any star cards. Write a simulation to approximate the probability that
your initial draw results in a final hand containing a diamond card.
"""


def prob_diamond(num_diam_in_hand, num_stars_in_hand,
                 num_diam_deck, num_stars_deck, num_reg_deck,
                 need_draw):
    """
    This function returns the probability of having a diamond card
    in your hand at the end of the process given the _current_ state
    of everything.

    State of your hand: `num_diam_in_hand`, `num_stars_in_hand`
    State of the deck:  `num_diam_deck`, `num_stars_deck`, `num_reg_deck`
    Other state:        `need_draw`
    """

    # If the deck is empty, we know the answer.
    # Right here the probability we have a diamond
    # is 1 or 0, depending on if we have a diamond. :)
    if num_diam_deck == num_stars_deck == num_reg_deck == 0:
        return 1.0 if num_diam_in_hand > 0 else 0.0

    # You first have to draw if need_draw > 0. You don't do other
    # logic at this point if you still need to draw.
    if need_draw > 0:

        total_p = 0.0

        total_cards_in_deck = num_diam_deck + num_stars_deck + num_reg_deck

        # We might draw a diamond:
        if num_diam_deck > 0:
            p = prob_diamond(num_diam_in_hand+1, num_stars_in_hand,
                             num_diam_deck-1, num_stars_deck, num_reg_deck,
                             need_draw-1)
            total_p += p * num_diam_deck / total_cards_in_deck

        # We might draw a star:
        if num_stars_deck > 0:
            p = prob_diamond(num_diam_in_hand, num_stars_in_hand+1,
                             num_diam_deck, num_stars_deck-1, num_reg_deck,
                             need_draw-1)
            total_p += p * num_stars_deck / total_cards_in_deck

        # We might draw a regular card:
        if num_reg_deck > 0:
            p = prob_diamond(num_diam_in_hand, num_stars_in_hand,
                             num_diam_deck, num_stars_deck, num_reg_deck-1,
                             need_draw-1)
            total_p += p * num_reg_deck / total_cards_in_deck

        return total_p

    # Otherwise, if you don't need to draw, we have to check the state
    # of your hand.
    else:

        # If you have star cards, you aren't done yet.
        if num_stars_in_hand > 0:
            # Discard the star card(s), and draw 3 more cards:
            p = prob_diamond(num_diam_in_hand, 0,
                             num_diam_deck, num_stars_deck, num_reg_deck,
                             3 * num_stars_in_hand)
            return p

        # Otherwise you are done. Right here the probability we have
        # a diamond is 1 or 0, depending on if we have a diamond. :)
        else:
            return 1.0 if num_diam_in_hand > 0 else 0.0


if __name__ == '__main__':

    print prob_diamond(0, 0,
                       3, 3, 60-3-3,
                       5)

