---
title: "FDA, 23andme, and Innovation"
date: 2013-11-26T09:21:00-05:00
comments: true
categories: [ "bioinformatics", "government" ]
draft: false
---

I'm neither a doctor nor a lawyer, so consider my opinions appropriately. I began my career as a software developer at the [Genome Institute (TGI)][0] at Washington University in St.Louis. I didn't set out to get into bioinformatics, it just happened that it was the most interesting problem to work on in [St.Louis][1] at the time I was getting my degree in computer science. So I set about learning the craft of software development and the field of bioinformatics at the same time. 

As many before me have noticed, biology and computers are strangely similar at their most basic level. Both decompose into some basic operations that get repeated over and over, with important results emerging at higher orders from the basic operations. Computer processors can only do simplistic operations on a few pieces of data at a time. Add two numbers. Multiply two numbers. Compare two numbers. [Algorithms][2] of enormous complexity can be implemented as a series of much smaller operations. Such is the case with biology. DNA is transcribed into RNA, which gets translated into proteins, which interact with each other in a cascading series of [pathways][3] that in the end results in the swarm of cells that is a human being.

So when I began working on the variant calling portion of the [cancer sequencing][4] pipeline at TGI, I started to see that not only are these two fields, computers and biology, deeply similar, but that they reinforce and supplement one another. Computers are to biology what the telescope was to astronomy. Both biology and astronomy existed before their defining technologies were invented, but neither would be nearly as valuable to mankind without their paradigm-shift enabling technologies.

I was intimately involved in the process of taking raw genomic data from a sequencing machine and shepherding it through the pipeline of steps required to produce some actionable output. In the case of cancer sequencing, the output is mostly studies on large aggregations of tumor samples to try and discover how varieties of cancer develop and spread. But sometimes the output is meant to used for clinical sequencing. This is the sequencing of [one specific person][5] and their tumor, to determine if the drugs we already have are good candidates for treatment. I was up to my elbows in other people's DNA. I saw the variants in their DNA that determine their health. It was like reading the source code for a human being. So naturally I became curious about my own DNA.

Enter [23andme][6].

23andme provides a personal genome service that can determine which variants an individual has at one million pre-selected sites in the genome. All you need to do is spit in a tube and mail it to them. A few weeks later they let you know when the sequencing and analysis is done, and you get to revel in the information about your source code, just like people with access to big labs, like TGI. To be sure, this is not the same as whole genome re-sequencing, where each and every base of the entire individual is determined. That is a bit more costly, but getting cheaper every day. 23andme provides answers to specific questions like "do I have the [BRCA mutations][7] which make me much more susceptible to breast cancer?" The answers you get from 23andme are answers to well studied questions.

By this time, I had become more involved in the field of bioinformatics and ended up at a commercial bioinformatics software shop here in St.Louis, [Partek Inc.][8] In order to fuel their employees' interest in genomics and spark their thinking on use cases, they paid for all of us to get sequenced by 23andme. So in the summer of 2012, we each received our results and marveled at the vast amount of detail. Each question answered by sequencing is backed up by a plethora of links to published journal articles describing the function and studies done on that particular variant. 

Here is how 23andme describes the state of my genome with respect to the above mentioned BRCA mutations:

>No copies of the three early-onset breast and ovarian cancer mutations identifiable by 23andme. May still have a different mutation in BRCA1 or BRCA2.

You have to be familiar with how genetics works in order to properly parse this statement.

Enter the [FDA][9]. The FDA has recently ordered 23andme to stop providing their service to consumers. One of the issues they cite, is providing BRCA data to consumers:

>For instance, if the BRCA-related risk assessment for breast or ovarian cancer reports a false positive, it could lead a patient to undergo prophylactic surgery, chemoprevention, intensive screening, or other morbidity-inducing actions, while a false negative could result in a failure to recognize an actual risk that may exist.

This is an alarming point to raise. No one wants to needlessly cause "morbidity-inducing actions" or give a false sense of security. So let's unpack both the false positive case and the false negative case. 

A false positive would be asserting that the customer has a specific mutation, when they do not in fact have that mutation. What are the odds of this happening? I don't have specific data on the 23andme lab, but similar technologies result in errors on the order of 2.5 calls in 100,000. This is indeed a small probability. This is in the neighborhood of flipping a coin and getting 16 heads in a row. It's quite unlikely, but not unthinkable. So if you get 1,000,000 variant calls from 23andme, somewhere in the neighborhood of 25 will be incorrect. There is a much deeper error model built around sequencing and variant calling, but I will only glance off the surface for today's purpose. The FDA is concerned that "morbidity-inducing actions", like a mastectomy, could be undertaken based on faulty evidence. However, very few customers of 23andme are going to read their results, find a BRCA positive answer, and immediately perform a self-mastectomy. At some point, the medical establishment gets involved. There are orthogonal methods of validating the BRCA carrier status. 23andme is purely an informational service, meant to be the beginning of a conversation, not the last word.

The case of a false negative is on the same order of improbability as the false positive. The snag comes in the semantics of the question being answered. Does the patient have the previously identified, inherited mutations in the BRCA genes? This is like knowing a certain edition of a book has a typo in a specific word on a specific line. Science has identified several of these specific typos that are commonly inherited. 23andme tells you if you have these specific typos in your book of life. It's also possible that you acquired a typo during your lifetime, in some other word in the BRCA chapter of your genome. Or even that you inherited a typo, but one that hasn't been identified by science yet. These are answers that 23andme can't give you. So while they can say you don't have typo's X,Y, or Z, they can't state that you have no typos at all. 23andme even states this in the copy on their site "May still have a different mutation in BRCA1 or BRCA2."

In effect, the FDA wishes to place some barrier, either themselves or some other apparatus of medical establishment, between your genome sequence and you. They call the service that 23andme provides a "medical device." I don't claim that the implications of consumer genome sequencing are clear or entirely knowable at this time. I do claim that if we step in with overreaching caution and control where it is not warranted, we risk destroying a nascent industry that is going to be one of the biggest most world-shaping technologies of the next 100 years. Companies that now enjoy the freedom to innovate with new products and technologies will be forced to move elsewhere or stop.

St.Louis is becoming an important center for life-sciences, with the Genome Institute, Monsanto, the [Danforth Plant Science Center][10], Partek, and even newer players like [Cofactor Genomics][11]. The path forward to the 21st century for these technologies does not go through slow, monolithic government bureaucracies. People free to act on their insights and recent innovations will build this industry elsewhere if we clamp down on it now. 

[0]: http://genome.wustl.edu/ "The Genome Institute"
[1]: http://www.articulateventures.com/articulate-blog/category/a-newcomers-view-of-st-louis-a-heroic-city "St.Louis"
[2]: https://en.wikipedia.org/wiki/BLAST "BLAST Algorithm"
[3]: https://en.wikipedia.org/wiki/Insulin_signal_transduction_pathway_and_regulation_of_blood_glucose "Insulin Pathway"
[4]: http://genome.wustl.edu/projects/category/cancer-genomics/ "Cancer Genomics"
[5]: http://www.forbes.com/sites/matthewherper/2011/12/16/christopher-hitchens-and-steve-jobs-mark-limits-of-dna-sequencing-technology/ "Christopher Hitchens and Clinical Sequencing"
[6]: https://www.23andme.com/ "23andme"
[7]: http://www.cancer.gov/cancertopics/factsheet/Risk/BRCA "BRCA mutations"
[8]: http://partek.com/ "Partek Inc."
[9]: http://www.fda.gov/ICECI/EnforcementActions/WarningLetters/2013/ucm376296.htm "FDA 23andme Letter"
[10]: http://www.danforthcenter.org/ "Danforth Plant Science Center"
[11]: http://www.cofactorgenomics.com/index.php "Cofactor Genomics"
