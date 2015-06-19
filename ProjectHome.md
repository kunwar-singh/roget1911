Roget's Thesaurus (1911 edition) contains a rich, structured collection of
semantic clusters -- words and/or short phrases, grouped together by close
semantic association. This project offers two derived documents:
**roget.xml** and **synlists.txt**.

**roget.xml** is a clean, human/machine readable version of the Thesaurus.
Available versions are very hard to work with:
formatting conventions are confused and inconsistent, and the text suffers
from a high error rate in their application.
We used a combination of machine-parsing and hand-editing
to produce a clean and consistent version.  Representation is in xml,
but the document object model is trivial, so you can easily write a little
program to read it in if you find xml parsers cumbersome. See RogetXml for
more information.

**synlists.txt** is a collection of synonym lists, intended for use
in keyword searches. You can easily pull raw synonym lists out of the
Thesaurus, but the results are not very useful -- the number of
lists is too large, and the overlap is too high. To create
useful synonym lists, we tore the raw lists apart and created
new ones, using word->list mappings that reflect the semantic associations
established by the Thesauru's document structure.
See SynLists for more information.

To see how this approach works out in practice, check out the Online Demo
at http://roget1911.appspot.com
This is an interactive thesaurus based on **synlists.txt**.

To download **roget.xml** and **synlists.txt**, click **Source** in the menu at
top. This takes you to the project Source page.  Click **Browse** to go to the
browse-source page, then click **Download zip**.  The zip file contains
**roget.xml** and **synlists.txt**, along with the resource files and Python
scripts used to construct them.