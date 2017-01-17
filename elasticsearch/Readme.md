# Create Mapping
1. `curl -XPUT 'http://localhost:9200/blog/' -d @post.mapping.json`

# Add post
1. `curl -XPOST http://localhost:9200/blog/post/ -d @post1.data.json`
1. `curl -XPOST http://localhost:9200/blog/post/ -d @post2.data.json`

# Search
1. simple
    1. `curl -XGET localhost:9200/blog/post/_search?q=name:tom`

1. with body
    1. `curl -XGET localhost:9200/blog/post/_search -d @post.query1.json`
    1. `curl -XGET localhost:9200/blog/post/_search -d @post.query2.json`

