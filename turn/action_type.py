from enum import Enum


class ActionType(Enum):
    """Main action could contain one of: attack or skill.
       Side action could contain determination or some_simple_unreleased stuff"""
    MAIN = 'main'
    SIDE = 'side'


