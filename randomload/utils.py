"""Module with random methods."""
import random


def randomname(prefix='random', l=6):
    """Generates random string name of hexadecimal characters.

    :param prefix: String to preprend to name
    :param l: Length of generated name.
    :returns: String
    """
    r = ''.join(random.choice('0123456789ABCDEF') for i in xrange(l))
    return '{0}-{1}'.format(prefix, r)


def randomfromlist(l):
    """Returns random item from list.

    :param l: List
    :returns: object|None
    """
    if not l:
        return None
    return l[random.randrange(len(l))]


def randomsample(l, sample_size=1):
    """Returns new list containing a random sample.

    :param l: List to sample from
    :param sample_size: Integer sample size
    :returns: List
    """
    return random.sample(l, sample_size)
