# Versioning
This project follows semantic versioning. Build numbers will not necessarily be factored in to versioning. This is because python is a dynamically typed, interpreted language that does not build machine code or generate executables natively. This project does however implement the standard features of semantic versioning. It is generally understood that semantic versioning practices are best suited to API's (as stipulated in rule 1 in the [semantic versioning website](https://semver.org )). However, it is a practice that I greatly admire and I believe that integrating semantic versioning and its practices into this codebase would give a much more comprehensive release history that lack thereof.   

## Introduction
First, I'll briefly cover semantic versioning as it pertains to API's. Please note that this is a shortened explanation and highly condensed into the fundamentals and doesn't necessarily include release candidates, pre-alpha releases, release code names, and so on.

You typically have 3 'branches' or 'numbers'. The **Major**, **Minor**, and **Patch** but it's actually much easier to think of them as **Major**, **Feature**, **Bugfix** branches, because that's really what they are. I've yet to rack my brain for a good replacement name for the Major branch in this example, so it'll stay that way for now. 

## Branching

As explained previously, each branch represents a change in the codes progression over time. Be the state one of repair, implementation or massive-implementation (as denoted by the major branch), it's generally considered good practice to notate release numbers by way of semantic-version control. 

### **Major**
When developing an **API**, the major version is incremented whenever there is a breaking change. A breaking change, as the name implies refers to a change that breaks things. 'Things' being previous versions. For example, if an API makes a change that removes a function, or refactors a function name, it would be considered a 'breaking change' because all of the projects that use that function would now have to either: 

 a) Stay with the previous versions as to not have to refactor

 b) Upgrade versions but refactor the code

_Most normal people choose the latter._

***Contingencies:*** Whenever a major branch is incremented, the minor and patch branch go back to 0. 

If you think of each branch as a sort of 'clock' that resets every time its parent (the number to its right) changes, then that makes it much easier to visualize. 

### **Minor**
The minor branch is incremented when a backwards compatible feature is added to a codebase. To continue on from the previous analogy, if a function was _added_ which then gave the library some additional functionality, then the minor branch would be incremented. 

Remember, the minor branch (represented in this case by) `Y`, is the number in the middle: `x.Y.z`. If I was at version `1.0.0` and I added a feature, the minor branch would go up. So the next release (the one containing the new feature) would be `1.1.0`.


### **Patch**
The patch or the 'bug-fix' branch, as it was named in the introduction, is a branch that is incremented whenever a bug-fix occurs. Typically, bug fixes are grouped together in releases so that the bug fix branch doesn't go up too high, but there is no real rule on how high a branch can go up. However, with that said, there's typically a limit for some programs when a branch number is greater than `255`. I'm not sure why its 255 exactly, possibly following the RGB number format?

The bug fix branch or the 'patch' branch is `Z` if we continue the example of `x.y.Z`. In reality `x` `y` and `z` would be numbers. Let's have a go at substituting these representations into actual numbers. Let's say that our current version is 0.1.0 (so it's in an alpha stage because we haven't made a significance release yet) and we have fixed a bug. We would increment the patch (bug-fix) branch to `0.1.1`. 

Remember, you can still fix multiple bugs and only increment the release by 1. Or, you could fix 3 bugs and make 3 separate releases. Your choice. Just remember to put in the release notes that you've fixed multiple bugs if you choose to go down that route. In fact, this applies to features as well. You can fix multiple features or even multiple features **and** multiple bugs and `z` would go to 0 (because we're incrementing its parent or 'feature branch') and `x` would increment by 1. 

## Modified Branching
Because this project is not an API, it uses a sort of 'modified' branching system in which branches are representative of similar things, but work in different ways. Most branches retain the same functionality except for the major branch. This is because it's impossible to have a backwards compatible change if you're not developing a library. However, a backwards compatible change in this case, would be considered something like removing a command or function in favor of a new one, or say, deprecating a function in favor of a new one. This would all be considered a breaking change and would rightly warrant the incrementalism of the major branch.
