#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import elasticsearch


def main():
    es = elasticsearch.Elasticsearch()
    response = es.search(index='blog', doc_type='post', body={
        "query": {
            "match_all": {}
        }
    })
    print(response)

if __name__ == '__main__':
    main()