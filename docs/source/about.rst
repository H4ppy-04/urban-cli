About Urban CLI
===============

Urban CLI was developed as a small portfolio side project while I was working at university. It was developed over a period of a week, in which I spent developing and refining this project to be as optimized and bug-free as possible.
As development ramped up, I realized that I wouldn't be able to separate code into chunks and files. It was at this point that I decided to test my code. This choice proved to be extremely useful.

Current Features
----------------
I plan to add definition examples under the definition itself. This has sort of been already mentioned in the issue/branch thread that is for this feature, however I'll state again that this feature will follow the same colorized format and conventions that the regular definitions have. If a word is colored, it means that word is also defined. The reason why words are colored is so that users know that they can look up that word next if they have an interest as to the meaning of that word in the urban dictionary.

There were plans to display likes and dislikes (or 'upvotes' and 'downvotes' depending on which part of the internet you come from) under definitions as well. This is unfortunately, pretty impossible because likes and dislikes are rendered after-the-fact and are not received in a request content object. This still remains an active function in the program in case this ever changes, and it will require minimal change to the code if the integration ever does happen, but as for now the function is decorated as deprecated.

Maintenance
------------
This project is fairly limited in scope and potential. If you're to consider something like a tkinter supported application/GUI that has various buttons and features, it would make sense to have an extensive roadmap. However, with something as limited as this, if there is no need to add extensive features, even if it's possible, I won't.

I essentially started with an idea, a fairly simple one, and now that's come to fruition and approaching the end of development, I feel no need to chart out extra goals or create anything that hasn't already been done. I'll still be fixing bugs, making optimizations and improving things. If you've just come from the semantic versioning page, this roughly translates to: I'll only ever be incrementing the patch branch and very rarely the feature branch for optimizations.
