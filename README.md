# link-fetcher-with-cookies


## Instructions

We need to run this 3 times.

```python
python3 get_links.py
```

The first time a simple login is required to save the cookie/profile data in the `user-data-dir`. The second time we get the `href`(s) off the homepage cards (courses). The third time we run this we grab all the links off the courses and save them in their own file. The bash script included will be useful for calling `youtube-dl` to download batches at a time.
