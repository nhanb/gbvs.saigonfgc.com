# Dev

TL;DR:

```sh
sudo pacman -S pandoc entr python

# rerun build script whenever a `README.md` or `template.html` file is updated:
find . \( -name README.md -o -name template.html \) | entr python build.py

# host static website locally at port 8000:
python -m http.server --bind localhost
```

This is a ghetto tatic site setup powered by pandoc and some glue code,
inspired by [this post][1].

The gist is that this whole repo is a ready-to-serve static website.
The **build.py** script looks for all files named **README.md** and run
`pandoc` on them, generating **index.html** files in the same place as their
respective markdown files.

Pros:

- Dead simple what-you-see-is-what-you-get site structure.
- Post-specific assets are put in the same dir as the post's md file. This
  allows simple relative image paths without stupid hacks (looking at you,
  Pelican!)
- Pandoc's markdown-to-html translator is simply better: automatic `<figure>`
  element for top-level images was why I considered pandoc in the first place.
- Maximum flexibility: I can already see how custom pages will be a breeze with
  this setup, since each page is extremely self-contained. I can finally do
  crazy stuff like [Zach Holman's blog][2].

Cons:

- No automatic index generation (that I know of).
- No RSS feed out of the box.

I'll need to tinker more.

[1]: https://skilstak.io/building-an-ssg-with-pandoc-and-bash/
[2]: https://zachholman.com/talk/utc-is-enough-for-everyone-right
