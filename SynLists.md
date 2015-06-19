**synlists.txt** is an ascii file containing 14,000 synonym lists,
constructed from the semantic associations contained in Roget's
Thesaurus (1911 edition).  Each list is comprised of one or more
"terms" -- either a single word, or a short phrase. There are 36,500
terms in toto: 26,000 are single words, the remaining consisting of
phrases.

You can easily pull raw synonym lists out of the Thesaurus, but the
results are not very useful -- the number of lists is too large, and
the overlap is too high.  We created **synlists.txt** by visiting each
list in the Thesaurus, tearing it apart, and assigning its terms to
one or more members of a dynamically generated collection of synonym
sets.  The result is a useful set of
synonym lists, that accurately reflects the semantic associations recorded
in the Thesaurus.

To see how this approach works in practice, see the Online Demo
at http://roget1911.appspot.com

Below gives details on how the lists were constructed.
We start with a quick description on the document structure of the
Thesaurus.

### Structure of the Thesaurus ###
The Thesaurus establishes 3 levels of semantic association. The
primary level is the synonym list -- one or more words and/or short
phrases, joined together with commas.
The secondary level is created by linking these lists together,
using  semi-colons as the separator character (We will refer to these
as "groups", meaning "a group of semantically related synonym lists").
The third level is established by organizing groups into sections.
There are 1047 sections in the Thesaurus, each corresponding to some
broad conceptual or ontological category.

An additional kind of association is created by cross references.
These are **section:keyword** pairs that appear in synonym lists, and
refer to words in other sections. Cross references provide important
information, but they are troublesome because they violate the hierarchal
scheme established by the document structure.  In this work we began
by creating a version in which cross references were expanded.
If the cross reference **[section:keyword]** appeared in a list, it was
removed and replaced by all lists, containing **keyword**, that appeared in
**section**.

### How the Lists Were Constructed ###
The basic strategy is:
```
  for each synlist "sl" in the Thesaurus
    -- compute "key" This is a function over (sl,group,section),
       where "group" is the group containing sl and "section" is the
       section containing the group.
    -- map each word in sl to key. 
  After all synlists have been visited, invert the mappings word->{keys},
  creating the mappings key->{wrds}. These give the new synonym lists.
```
**key** is computed from (**sl**,**group**,**section**), using the notion
of "most significant word". We define a function, "mostSigWord",
which accepts a collection of words (**words**) and a section
(**section**) as arguments and selects the most significant word in
**words**.
```
  mostSigWord(words,section):
    Select most-significant word in "words". Criteria are (in
    descending order of significance):
    1. w1 is more significant than w2 if it appears more frequently
       in "words"
    2. If w1 and w2 appear with equal frequency in "words", w1
       is more significant than w2 if it appears more frequently in 
       "section".
    3. If w1 is less than w2 in lexigraphic order, choose w1
```
**key** is then defined as the word pair:
```
  key = [mostSigWord(sl,section), mostSigWord(group,section)]  
```
Inverting the mappings **key->{words}** gives our first cut at the lists.
We refactor them in several ways to increase their accuracy in keyword
searches. The major refactoring involves the notion of "supermappings".
Suppose there are 2 mappings, **key1->{words1}** and **key2->{words2}**. If
**{word1}** is "large" (say, has 4 or more members), and **{words1}** is
a subset of **{words2}**, then the second mapping (established by **key2**)
is a supermapping for the first. We can increase the accuracy of matches
(at the expense of number-of-hits) by removing the elements in **{words2}**
which occur in **{words1}**.