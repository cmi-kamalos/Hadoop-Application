# Hadoop-Application

This repo is built through following the course of Hadoop Platform and Application Framework on coursera proposed by University of California San Diego. They covered the essentials of Big Data platform and provided hands-on application on realtime project. Despite I have been Certified IBM Big Data. I noticed a small difference in those training programs. IBM embedded the learning process on their platform through virtual lab. It's practical but it abstracts a lot of exposure that it could beneficial to the trainee.
## Motivation
The principal drive and urge is to facilitate certain tasks that can be easy unbearable for new comer who happened to be beginner into hadoop and linux environment. Though he could be following the theorical part of the course but he'll have hard time applying these skills when it comes to practice.
Because the course is a little bit outdated or just the different setups are no longer working as expected.

**Disclaimer**: I have no affiliation to the program, I help simply as I could to make the learning path easier. It could help you save great time without enduring any hustle.

## Setup
Before starting the learning journey , you must setup your hadoop environment. We'll be using cloudera in a virtual env. It's better to download virtual box(vbox) version from cloudera website. Although it's possible to use vmware as used in the course. Stick with me with a vbox. It has advantage when customizing its parameters. That's the advantages over vmware (free version).

1- Download cloudera on the following link: https://downloads.cloudera.com/demo_vm/virtualbox/cloudera-quickstart-vm-5.13.0-0-virtualbox.zip. honestly it's going to an end  of support. We'll be sticking as close as possible with the course. Otherwise, if you fill comfortable use **CDP**.

2- You'll have to update your cloudera VM as the centos running cloudera reached the end of life. There is a tuto explanation of the process (https://data-mining.philippe-fournier-viger.com/how-to-update-the-cloudera-vm-solved/?unapproved=35099&moderation-hash=56ec7d1b8ba9a33cf5ea241c0182e99d#comment-35099 ). Skip this step if you don't use **cloudera cdh quickstart**

3- After that migrate your python from python 2.6 to at least 2.7 to be effectively use pip or easy_install.

4- Install vbox guest additions. while on parameter go **general > advanced** enable shared clipboard to **bidirectional**. Increase your vbox ram and cpu to double of the initial config if allowed.

## Execution of simple mapreduce operation
 In this simple example, we'll walk-through a counting problem using mapreduce. The idea is to emphasize on the key-value as core of this paradigm. The code will be on the folder **wordcount_mapreduce**. The steps of the resolution will be on the following:
 
 I) Create the mapper that will run on the dataNode. A little precision as we're progressing ( we don't have a cluster of nodes, it means 1 dataNode). The mapper map all key-values elements from our input files: "wordcount_mapper.py"
 
 II) Create a reducer that will iterate over elements which happened to have the same key. It counts those elements and reduce them: "wordcount_reducer.py"
 
 III) Make Files which contain the words to count. In terminal: 
 
    echo "A long time ago in a galaxy far far away" > testfile1
 
 IV) Elevate permission for the mapper and reducer to be executable: 
 
    chmod +x wordcount_mapper.py
    chmod +x wordcount_reducer.py
 
 V) Create a directory for the user input and put Files containing those words into  Hadoop : 
 
    hdfs dfs -mkdir /user/cloudera/input
  
    hdfs dfs -put ~/testfile* /user/cloudera/input
 VI) Test the program in local (always in terminal) : 
 
    cat testfile* | python wordcount_mapper.py | sort | python wordcount_reducer.py
 
 VII) Final execution by the following syntax:
 
    hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/cloudera/input/testfile1 -input /user/cloudera/input/testfile2 -output /user/cloudera/output_new   file ~/wordcount_mapper.py -mapper wordcount_mapper.py file ~/wordcount_reducer.py -reducer wordcount_reducer.py
    
 VIII) Export result into your local from hadoop environment
 
    hdfs dfs -getmerge /user/cloudera/output_new/*  wordcount_num1_output.txt
