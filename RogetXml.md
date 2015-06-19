**roget.xml** is an ascii text file containing an xml version of Roget's
Thesaurus (1911 edition). Roget offers a rich, structured collection of semantic
clusters -- words and/or short phrases, grouped together by close semantic
association.  Unfortunately, available versions are very hard to work with.
Formatting conventions are confused and inconsistent, and the text suffers
from a high error rate in their application. **roget.xml** is a clean,
human/machine readable version of the 1911 edition. Representation is in xml,
but the document object model is trivial, so you can easily write a little
program to read it if you find xml parsers cumbersome.

## Source Text Document Structure ##
### Synonym lists, Groups, and Sections ###
Roget's fundamental data structure is the synonym list.  A list consists of
one or more words and/or short phrases, joined together with commas.
Example: "babyhood, childhood, boyhood, girlhood".
Roget then creates a secondary level of semantic
association by linking together synonym lists, using semi-colons to join the
lists. We will refer to these as "groups". Each group is assigned a
part-of-speach attribute.  Possibilities are:  N, V, Adj, and Adv, meaning
Noun, Verb, Adjective, and Adverb.

Roget establishes a third and final level of semantic association by
collecting groups into sections. Sections have evocative titles:
the first is titled "Existence", the second is titled "Inexistence", while
the last is titled "Temple". Each section corresponds to some broad
conceptual or ontological category.

The semantics of this structure is (loosely): a synonym list corresponds to
a "sense"; a group is collection of related senses; a section is a
conceptual or ontological category, to which the senses are relevant.

### Cross References ###
Cross references occur frequently in the text. Sometimes they
refer to locations within the current section ("intra-sectional"); other times
they consist of a (word,sectionId) pair referencing locations in other
sections ("inter-sectional"). Roget uses cross references to establish semantic
associations that cut across the section/group/synonym list schema described
above. We found the intra-sectional references to
be too vague to be of use, and eliminated them in the xml version.
Inter-sectional references were retained.

### Other Data ###
The text contains markups giving synonyms drawn from a handful
of non-English European languages.  It also contains example phrases taken from
literature. These were all eliminated in the xml version.

## roget.xml Document Structure ##
The top level node is labeled "roget". Its child nodes
are all labeled "section". Each section node has an "id" and "title"
attribute. Usually the id is just a number ("1","2",etc.) but sometimes
Roget's original classes were subdivided, so (for example) there is one
section named "20", and another named "20a".

Each section has 4 subsections, each associated with part-of-speach.
These are labeled N, V, Adj, and Adv.

Each part-of-speach subsection contains one or more group nodes,
labeled "g". These contain synonym lists.  Each group node has an
"id" attribute. The id gives the section id, part-of-speach, and
group-enumerator associated with the node. Here is an example of a group
node.
```
<g id="287.N.1">
  recession, retirement, withdrawal;
  retreat;
  departure;
  #277:recoil;
  flight #623:avoidance;
</g>
```
The id of this node is "287.N.1". Reading from left to right, this means:
  * the node belongs to the section named "287"
  * part-of-speach is "N", meaning "noun"
  * this is the first N group for section 287
This example contains two cross references. "#277:recoil" references
section 277, with keyword "recoil". "#623:avoidance" references section
623, with keyword "avoidance". Note that the second ref is preceded by the
work "flight". This is a common pattern, and seems to imply some association
between the word "flight" and the referenced content. But one also
encounters:
```
<g id="289.V.1">
  repel, push from, drive apart, #276:drive_from;
  chase, dispel;
  abduct;
  send away;
  repulse;
</g>
```
Here the reference is preceded by a comma. We can't tell whether the
presence or absence of a comma before a reference is meaningful or not,
so the xml simply echoes the source text.