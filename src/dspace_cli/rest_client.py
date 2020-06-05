# -*- coding: utf-8 -*-

"""Rest client for DSpace."""
from collections import Set
import requests
from .config import config

def create_community(community_name: str) -> str:
    """Create a community in DSpace. A community groups collections for an entity.
    Exampes could be Departments, Labs, Research Centres or Schools.
    :param community_name: name for the community
    """
    return requests.get(config["dspace"]["dspace-url"])

def create_collection(communities: Set, collection_name: str):
    """Create a collection in DSpace. A community groups collections for an entity.
    Exampes could be Departments, Labs, Research Centres or Schools.
    :param community_name: a list of communities to attach the collection to.
    :param collection_name: name of the collection.
    """