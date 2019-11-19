#!/usr/bin/bash/python3
#################################################################
# Part 0
# Prepare
import subprocess
import re
import pandas as pd
import readline
# Print colored text
green='\033[1;32m'
blue='\033[34m'
yellowb='\033[1;33m'
yellow='\033[33m'
purple='\033[2;35m'
cyan='\033[1;2;36m'
red='\033[31m'
# Reset colors
end='\033[m'
# Title
print(yellowb+"\n-------------------------------------------------------------------------------"+end)
print(yellowb+"                      Analysing Your Protein Sequences                         "+end)
print(yellowb+"\n                              BPSM Assignment2                                 "+end)
print(yellowb+"-------------------------------------------------------------------------------\n"+end)

##################################################################
# Preparation
print(red+"* Important:"+end)
print("\nThis programme is designed to analyse protein sequences. Users are allowed to identify a family of protein sequences from a user-defined subset of the taxonomic tree (e.g. glucose-6-phosphatase proteins from Aves (birds), or ABC transporters in mammals, or kinases in rodents, or adenylcyclases in vertebrates etc.) that could then be processed using, for example, one or more of the EMBOSS programmes. Therefore, you should:\n")
print("(1) Prepare your protein dataset, including the protein family and the taxonomic group.\n(2) Install Python3, EDIRECT, CLUSTALO, MAKEBLASTDB, BLASTP, EMBOSS programmes (such as 'cons', 'plotcon', 'patmatmotifs', etc.)")
print(purple+"\nIf you have done all of the preparatory work, you can start now! "+end)
print(green+"\nPart 0: Preparation"+end)
while True:
    choice0=input(cyan+"\n1. Are you ready to start now? (y/n): "+end)
    if choice0.lower()=='y':
       break
    else:
       if choice0.lower()=='n':
          print("\nYou can start later when you are well prepared.")
          choice00=input(cyan+"\n2. Do you want to exit? (y/n): "+end)
          if choice00.lower() == 'y':
             print("\nYou can start again whenever you are well prepared.\n\nSee you next time! Have a nice day!\n")
             exit()
          else:
             if choice00.lower() == 'n':
                print("\nYou can start later when you are well prepared.")
             else:
                print(yellow+"\nwarning: You haven't typed in the corrected format. You can only type either 'y' or 'n'. Please start again!"+end)
       else:
          print(red+"\nERROR: You didn't type in the corrected format. You can only type either 'y' or 'n'. Please start again!"+end)
############################################################################################################################
# Part 1
# 1. Let the users to specify the protein family and the taxonomic group
print(green+"\nPart 1: Confirm the dataset"+end)
print(green+"\n1. specify the protein family and the taxonomic group."+end)
# Check the contents of input
while True:
    # (1) Let users to specify the protein family
    test_protein=input(cyan+'\n(1) Please select your protein family: '+end)
    if re.search(',',test_protein):
       print(red+"\nERROR: Your input contains special character(s). Please check carefully and start again!"+end)
       continue
    else:
       # (2) Let users to specify a taxonomy group
       taxon=input(cyan+'\n(2) Please select a taxonomic group: '+end)
       if re.search(',',taxon):
          print(red+"\nERROR: Your input contains special character(s). Please check carefully and start again!"+end)
          continue
       else:
       # Tell the users how many sequences are found
       # This code can only be executed by Python3 not Pyhton2!
          print("\nHere is some information about the protein you are searching: ")
          number_sequences=subprocess.getoutput('esearch -db protein -query "{} AND {}[organism]" | xtract -pattern ENTREZ_DIRECT -element Count'.format(test_protein,taxon))
          number_species=subprocess.getoutput('esearch -db taxonomy -query "{}" | xtract -pattern ENTREZ_DIRECT -element Count'.format(taxon))
          # (a) If the number of sequences is 0 or 1:
          if int(number_sequences)<2:
             print(yellow+"\nwarning: Sorry! "+end+red+"No"+end+yellow+" sequence is found by searching "+end+purple+test_protein+end+yellow+" and "+end+purple+taxon+end+yellow+". Please check if you have typed the correct names and then start again to select another protein family or taxonomic group."+end)
             extra=input("\nDo you want to try again (t) or exit (e)? (t/e):")
             if extra.lower()=='t':
                print("\nPlease select another protein family or taxonomic group.\n")
                continue
             else:
                if extra.lower()=='e':
                   print("\nSee you next time. Have a nice day!\n")
                   exit()
                else:
                   print(red+"\nERROR: You didn't type in the corrected format. You can only type either 'y' or 'n'. Please start again!"+end)
          else:
             print("\n(a) There is(are) "+purple+number_sequences+end+" sequence(s) found in total.")
             # (b) If the number of sequences is no less than 10,000:
             if int(number_sequences) > 10000:
                print(yellow+"\nwarning: As your staring sequence set is bigger than 10,000, I suggest you not to continue. (But if you choose to continue, I will give you several options later and strongly recommend you to narrow down your scale.)"+end)
                # (3) Give users options to continue or not continue with the current dataset (sequences)
                choice1=input(cyan+"\nDo you want to continue with the current dataset? (y/n): "+end)
                if choice1.lower()=='y':
                   # Tell the users how many species are represented in the dataset chosen by them
                   print("\n(b) There is(are) "+purple+number_species+end+" species found in total.")
                   # (a) If the number of species is 0:
                   if int(number_species) == 0:
                      print(yellow+"\nwarning: Sorry! No species is found by searching "+taxon+". Please start again and select another protein family or taxonomic group."+end)
                      continue
                   else:
                      # (b) If the number of species is not 0:
                      print("\nThe species which contain(s) the protein sequences:\n")
                      subprocess.call('esearch -db taxonomy -query {} | efetch -format txt > taxonomy.txt'.format(taxon), shell=True)
                      taxonomy_txt=open("taxonomy.txt").read().rstrip('\n')
                      print(taxonomy_txt)
                      # (4) Give users options to continue or not continue with the current dataset (species)
                      choice12=input(cyan+"\n(3) Do you want to continue with the current dataset? (y/n): "+end)
                      if choice12.lower()=='y':
                         print("\nOk, you will go on to the next step! ")
                         break
                      else:
                         if choice12.lower()=='n':
                            choice13=input(cyan+"\nDo you want to start again (s) or exit (e)? (s/e): "+end)
                            if choice13.lower()=='s':
                               print("\nPlease start again and choose another protein family or taxonomy group this time.")
                               continue
                            else:
                               if choice13.lower()=='e':
                                  print("\nSee you next time! Have a nice day!\n")
                                  exit()
                               else:
                                  print(red+"ERROR: You didn't type in the corrected format. You can only type either 's' or 'e'. Please start again!"+end)
                                  continue
                         else:
                            print(red+"ERROR: You didn't type in the corrected format. You can only type either 'y' or 'n'. Please start again!"+end)
                            continue
                else:
                   if choice1=='n':
                      choice11=input(cyan+"\nDo you want to start again or exit? (s/e): "+end)
                      if choice11=='s':
                         print("\nPlease start again and choose another protein family or taxonomy group this time.")
                         continue
                      else:
                         if choice11.lower()=='e':
                            print("\nSee you next time! Have a nice day!\n")
                            exit()
                         else:
                            print(red+"ERROR: You didn't type in the corrected format. You can only type either 's' or 'e'. Please start again!"+end)
                            continue
             # (c) If the number of sequences is less than 10,000
             else:
                print("\nYour staring sequence set is already smaller than 10,000. But you can also choose to narrow down the scale later if you want!")
                print("\n(b) There is(are) "+purple+number_species+end+" species found in total.")
                # (a) If the number of species is 0:
                if int(number_species) == 0:
                   print(yellow+"\nwarning: Sorry! No species is found by searching "+taxon+". Please start again and select another protein family or taxonomic group."+end)
                   continue
                else:
                # (b) If the number of species is not 0:
                   print("\nThe species which contain(s) the protein sequences:\n")
                   subprocess.call('esearch -db taxonomy -query {} | efetch -format txt > taxonomy.txt'.format(taxon), shell=True)
                   taxonomy_txt=open("taxonomy.txt").read().rstrip('\n')
                   print(taxonomy_txt)
                   # (3) Give users options to continue or not continue with the current dataset (species)
                   choice12=input(cyan+"\n(3) Do you want to continue with the current dataset? (y/n): "+end)
                   ####################################################################################################################################
                   if choice12.lower()=='y':
                      print("\nOk, we will go on to the next step! ")
                      break
                   ####################################################################################################################################
                   else:
                      if choice12.lower()=='n':
                         choice13=input(cyan+"\nDo you want to start again or exit? (s/e): "+end)
                         if choice13.lower()=='s':
                            print("\nPlease start again and choose another protein family or taxonomy group this time.")
                            continue
                         else:
                            if choice13.lower()=='e':
                               print("\nSee you next time! Have a nice day!\n")
                               exit()
                            else:
                               print(red+"\nERROR: You didn't type in the corrected format. You can only type either 's' or 'e'. Please start again!"+end)
                               continue
                      else:
                         print(red+"\nERROR: You didn't type in the corrected format. You can only type either 'y' or 'n'. Please start again!"+end)
                         continue     
print(green+"\n2. Narrow down the searching scale."+end)
# Add: Ask users if they want to select just one of the species in the chosen taxonomy group
while True:
    if int(number_species) > 1:
       print(cyan+"\n(1) As there are at least 2 species found in the taxonomy database, you can choose one of them as the study object."+end)
       print(cyan+"\n(2) Which species do you want to choose? "+end+yellow+"\n\nwarning: You can "+end+red+"only"+end+yellow+" choose one of them and type the"+end+red+" number"+end+yellow+" before the species you want to study.\n"+end)
       print(cyan+taxonomy_txt+end)
       choice2=input(cyan+"\nPlease input the number: "+end)
       if choice2.isdigit():
          if int(choice2) in range(1,int(number_species)+1):
             ######################################################
             file3=open('taxonomy.txt').read().rstrip().split('\n')
             outfile=open('species_file','w')
             for line in file3:
                 for i in range(1,int(number_species)+1):
                     if line.startswith(str(i)):
                        outfile.write(line)
                     else:
                        outfile.write('\n')
             outfile.close()
             # Make a dataframe using pandas modules
             df=pd.read_csv('species_file',header=None,names=["s"])
             df.dropna(inplace=True)
             new=df["s"].str.split(". ",n=1,expand=True)
             df["number"]=new[0]
             df["species"]=new[1]
             df.drop(columns=["s"],inplace=True)
             n_lst=df.iloc[:,0].values.tolist()
             s_lst=df.iloc[:,1].values.tolist()
             taxid_lst=''
             taxid=subprocess.getoutput("esearch -db taxonomy -query {} | efetch -format docsum | xtract -pattern DocumentSummary -element TaxId".format(taxon))
             taxid_lst=taxid.split("\n")
             species_dict1=dict(zip(n_lst,s_lst))
             species_dict2=dict(zip(n_lst,taxid_lst))
             object=species_dict1[choice2]
             id=species_dict2[choice2]
             print("The species you chose is "+purple+object+end+", and its TaxId is "+purple+id+"."+end)
             taxid_sequences=subprocess.getoutput('esearch -db protein -query "txid{}[Organism:exp] AND {}" | xtract -pattern ENTREZ_DIRECT -element Count'.format(id,test_protein))
             if int(taxid_sequences) < 2:
                print(yellow+"\nSorry! No or only 1 sequence is found by searching "+end+purple+test_protein+end+" and the TaxId of "+object+"is: "+purple+id+end+".")
                choice3=input(cyan+"\n(3) Would you like to choose another species (c) or exit (e)? (c/e): "+end)
                if choice3.lower() == 'c':
                   print("\nPlease try again and choose another species.")
                   continue
                else:
                   if choice3.lower() == 'e':
                      print("\nSee you next time. Have a nice day!")
                      exit()
                   else:
                      print(red+"\nERROR: You didn't type in the corrected format. You can only type either 'c' or 's' or 'e'. Please start again!"+end)
                      continue
                #################################################################
             else:
                print("\nThere are "+purple+taxid_sequences+end+" sequences found by searching "+end+purple+test_protein+end+" and the TaxId of "+object+"is: "+purple+id+end+".")
                break
          else:
             print(red+"\nERROR: You didn't type a number in the reasonable range. Please try again!"+end)
             continue                          
       else:
          print(red+"\nERROR: Your answer contains other special character(s) or not an integer."+end+yellow+"\n\nwarning: You can "+end+red+"only"+end+yellow+" choose one of them and type the"+end+red+" number"+end+yellow+" before the species you want to study. Please try again!"+end)
          continue 
    else: 
       id=subprocess.getoutput("esearch -db taxonomy -query {} | efetch -format docsum | xtract -pattern DocumentSummary -element TaxId".format(taxon))
       print("\n(1) As there is only 1 species found in the taxonomy database. You can go on to the next step to narrow down the scale if you like!")
       print("\nThe TaxId of the only"+purple+" 1"+end+" species found in the taxonomy database by searching "+purple+taxon+end+" is "+purple+id+end+".")
       break
             
# (4) Ask the users if they want to narrow down the scale. And choices are be given for users.
while True:
    a=input(cyan+"\n(2) Do you want to narrow down the scale? (y/n): "+end+yellow+"\n\nNOTE: 2 choices will be given for you later: \n(a) Type the name of a specific protein; \n(b) Choose the not partial sequences."+end+cyan+"\n\nDo you want to narrow down the scale? (y/n): "+end)
    if a.lower()=='y':
       methods=input(cyan+"\n(3) Which choice do you want to choose? (a/b): \n\n(a) Type the name of a specific protein; \n(b) Choose the not partial sequences.\n\n(a/b): "+end)
       if methods.lower()=='a':
          specific_protein=input(cyan+"\n(4) Please change the name of the protein family you chose before to a specific protein: "+end)
          specific_number=subprocess.getoutput('esearch -db protein -query "{}[TITL] AND txid{}[Organism:exp]" | xtract -pattern ENTREZ_DIRECT -element Count'.format(specific_protein,id))
#[Part 2: Get the fasta file of the not partial sequence.]
          subprocess.call('esearch -db protein -query "{}[TITL] AND txid{}[Organism:exp]" | efetch -db protein -format fasta > unaligned.fa'.format(specific_protein,id),shell=True)
          if int(specific_number)<2:
             print(yellow+"\nI am sorry! There is"+end+red+" no or only 1"+end+yellow+" sequence found in the database. \n\nwarning: Please check if you typed the correct names of the specifc protein. "+end)
             choice5=input(cyan+"\n(5) Do you want to try again (t) or exit (e)? (t/e): "+end)
             if choice5.lower() == 't':
                print("\nPlease check carefully or choose another specific protein this time. ")
                continue
             else:
                if choice5.lower() == 'e':
                   print("\nSee you next time. Have a nice day!\n")
                   exit()
                else:
                   print(red+"\nERROR: You didn't type in the corrected format. You can only type either 't' or 'e'. Please start again!"+end)
                   continue 
          else:
             print("\nHere is some information about the protein you are searching: ")
             print("\nThere is(are) "+purple+specific_number+end+" sequence(s) found in total.")
############ 
             # Add a safety option to users if the number of sequences is still over 10,000.
             if int(specific_number) > 10000:
                choice6=input(cyan+"\n(5) Do you want to continue with the current dataset? (y/n)"+end+yellow+" \n\nwaring: As the number of the sequences is still over 10,000, I suggest you not to continue or choose another method later. \n\n(y/n): "+end)
                if choice6.lower()=='y':
                   break
                else:
                   if choice6.lower()=='n':
                      choice7=input(cyan+"\n(6) Do you want to choose another method to narrow down the scale (c) or exit (e)? (c/e): "+end)
                      if choice7.lower() == 'c':
                         print ("\nPlease choose another method to narrow down your scale.") 
                         continue
                      else:
                         if choice7.lower() == 'e':
                            print("\nSee you next time. Have a nice day!\n")
                            exit()
                         else:
                            print(red+"\nError: You did't type in the corrected format."+end+yellow+" \nwarning:You can only type either 'c' or 'e'. Please start again!"+end)
                            continue
                   else:
                      print (red+"\nError: You did't type in the corrected format."+end+yellow+" \nwarning:You can only type either 'y' or 'n'. Please start again!"+end)
                      continue
             else:
                print("\n(5) As the number of the sequences is less than 10,000 now, you can go on to the next step.")
                choice8=input("\n(6) Do you want to continue (c) or or exit (e)? (c/e): ")
                if choice8.lower() == 'c': 
                   break
                else:
                   print("\nSee you next time. Have a nice day!\n")
                   exit()
############
       else:
          if methods.lower()=='b':
             not_partial_number=subprocess.getoutput('esearch -db protein -query "{} AND txid{}[Organism:exp] NOT PARTIAL" | xtract -pattern ENTREZ_DIRECT -element Count'.format(test_protein,id))
#[Part 2: Get the fasta file of the not partial sequence.]
             subprocess.call('esearch -db protein -query "{} AND txid{}[Organism:exp] NOT PARTIAL" | efetch -db protein -format fasta > unaligned.fa'.format(test_protein,id),shell=True)
             if int(not_partial_number)<2:
                print(yellow+"\nI am sorry! There is "+end+red+"no or only 1"+end+yellow+" not partial sequence found in the database. You can change another method to narrow down the scale. "+end)
                choice9 = input("\n(3) Do you want to change another method (c) or exit (e)? (c/e): ")
                if choice9.lower() == 'c':
                   print("\nPlease change another method to narrow down the scale. ")
                   continue
                else:
                   if choice9.lower() == 'e':
                      print("\nSee you next time. Have a nice day!\n")
                      exit()
                   else:
                      print(red+"\nError: You did't type in the corrected format."+end+yellow+" \nwarning:You can only type either 'c' or 'e'. Please start again!"+end)
                      continue 
             else:
                print (cyan+"\n(3) You have chosen to use not partial sequences.\n\nHere is some information about the not partial sequences you are searching: "+end) 
                print("\nThere is(are) "+purple+not_partial_number+end+" sequence(s) found in total.")
#################
                # Add a safety option to users if the number of sequences is still over 10,000.
                if int(not_partial_number) > 10000:
                   choice10=input(cyan+'\n(4) Do you want to continue with the current dataset? (y/n)"+end+yellow+" \n\nwarning: As the number of the sequences is still over 10000, I suggest you not to continue or choose another method later. \n\n(y/n): '+end)
                   if choice10.lower()=='y':
                      break
                   else:
                      if choice10.lower()=='n':
                         choice11=input(cyan+"\n(5) Do you want to choose another protein family / taxonomic group (c) or exit (e)? (c/e): "+end)
                         if choice11.lower() == 'c':
                            print ("\nPlease choose another method to narrow down your scale.") 
                            continue
                         else:
                            if choice11.lower() == 'e':
                               print("\nSee you next time. Have a nice day!\n")
                               exit()
                            else:
                               print("\nYou haven't typed in the corrected format. \nNOTE:You can only type either 'c' or 'e'. Please start again!")
                               continue
                      else:
                         print (red+"\nError: You did't type in the corrected format."+end+yellow+" \nwarning:You can only type either 'y' or 'n'. Please start again!"+end)
                         continue
                else:
                   print(cyan+"\n(4) As the number of the sequences is less than 10000 now, you can go on to the next step."+end)
# Ask users if they want to continue in the While Loop
                   choice12=input(cyan+"\n(5) Do you want to continue (c) or or exit (e)? (c/e): "+end)
                   if choice12.lower() == 'c': 
                      break
                   else:
                      if choice12.lower() == 'e':
                         print("\nSee you next time. Have a nice day!\n")
                         exit()
                      else:
                         print (red+"\nError: You did't type in the corrected format."+end+yellow+" \nwarning:You can only type either 'c' or 'e'. Please start again!"+end)
                         continue
                         
###################
          else:
             print (red+"\nError: You did't type in the corrected format."+end+yellow+" \nwarning:You can only type either 'a' or 'b'. Please start again!"+end)
             continue
    else:
       if a.lower()=='n':
##############
#[Part 2: Get the fasta file of the original protein family.]
          subprocess.call('esearch -db protein -query "{} AND txid{}[Organism:exp]" | efetch -db protein -format fasta > unaligned.fa'.format(test_protein,id),shell=True) 
##############
          break
       else:
          print (red+"\nError: You did't type in the corrected format."+end+yellow+" \nwarning:You can only type either 'y' or 'n'. Please start again!"+end)
          continue

# Part 2
print(green+"\nPart 2: Conservation Analysis among Protien Sequences."+end)
# Create a test sequence using clustalo
# Make a function using "def". And the output will got to the screen and be saved as a file output
def clustalo_results(unaligned_fa,aligned_msf): 
    subprocess.call('clustalo -i {} -o {} --outfmt msf'.format(unaligned_fa,aligned_msf),shell=True)
    subprocess.call('clustalo -i {}'.format(unaligned_fa),shell=True)
# Align the sequences in the fasta files by "clustalo"
while True:
    print(yellow+"\nwarning: The next step is to align your protein sequences using clustalo. If your sequence set is too big, this process will take a few minutes or longer."+end)
    choice13=input(cyan+"\nDo you want to continue with the current dataset or exit? (c/e): "+end)
    if choice13.lower() == 'c':
       print(green+"\n1. Now we are going to align your protein sequences using clustalo, and the output will go to the screen and also be saved as an msf file.\n\nThis process may take a few minutes. Please be patient.\n\nThe output: \n"+end)
       clustalo_results('unaligned.fa','aligned.msf')
       break
    else:
       if choice13.lower() == 'e':
          print("\nSee you next time. Have a nice day!\n")
          exit()
       else:
          print("\nYou haven't typed in the corrected format. \nNOTE:You can only type either 'c' or 'e'. Please start again!")
          continue
# Get a consensus sequence from a multiple alignment by 'cons' from EMBOSS
print(green+"\n2. Run BLASTP. Then check and limit the number of hits before the conservation analysis and plotting."+end)
print(green+"\nStep 1: Create a consensus sequence (test sequence) from the multiple alignment by 'cons' from EMBOSS\n"+end)
subprocess.call('cons -sequence {} -outseq {}'.format('*.msf','aligned.cons'),shell=True) 
# Show the consensus sequence on the screen.
print('\nThe consensus sequence: \n')
consensus_sequence=open('aligned.cons').read().rstrip('\n')
print(consensus_sequence)
# BLASTP
# Make a database
print(green+"\nStep 2: Make a database of the protein sequences in the fasta file: "+end)
subprocess.call('makeblastdb -in {} -dbtype prot -out {}'.format('*.fa','protein_sequences'),shell=True) 
# Run blastp of our consensus sequence (test sequence) against the protein_sequences database, using default parameters, and save the output to the file blastoutput.out
subprocess.call('blastp -db {} -query {} -outfmt 6 > blastoutput.out'.format('protein_sequences','aligned.cons'),shell=True) 

# Have a look at the output
print(green+"\nStep 3: The output has been saved to the file 'blastoutput.out'.\n\nHave a look at the output: \n"+end)
subprocess.call('more {}'.format('blastoutput.out'),shell=True) 
# Extract the number of hits in the blastoutput.out file   
blast=open('blastoutput.out').read().rstrip('\n').split('\n')
# Use pandas to add headers and sort with identities
df2=pd.read_csv('blastoutput.out',sep="\t",na_values=['-'],header=None,names=["EMBOSS_001","ACCN","identities","a","b","c","d","e","f","g","h","i"])
blast2=df2.sort_values('identities',ascending=False)
n=0
total_headers=""
hits_250=""
# Check the number of hits in the blastoutput.out file
print(green+"\nStep 4: Check the number of hits in the blastoutput.out file."+end)
for line1 in blast2.iloc[:,1]:
    header=line1
    total_headers += header+"\n"
    n=n+1
print('\n'+purple+str(n)+end+' hit(s) are found.')
if n == 0:
   print(yellow+"\nI am so sorry! There is no hit found. Although the possibility is very low, it happens! As we cannot go on to the conservation analysis, you have to exit or you can start the programme again if you want! \n\nSee you next time! Have a nice day! "+end)
   exit()
else:
   if n < 251:
      print ("\nAs the number of hits is no more than 250, we are going to do the conservation analysis and plotting using these sequences.")
      # For those sequences whose number is no more than 250: Draw a plot of protein conservation based on the alignment similarities
      print(green+"\n3. Draw a plot of protein conservation based on the alignment similarities by plotcon using EMBOSS.\n"+end)
      subprocess.call('plotcon -sequences {} -winsize 4 -graph svg'.format('*.msf'), shell=True)
      print("\nNow the plot has been successfully created and can be seen in 'plotcon.svg'\n")

# Part 3: For protein sequences whose number is no more than 250: Scan protein sequence(s) with motifs from the PROSITE database
      print(green+"\nPart 3: Scan protein sequence(s) with motifs from the PROSITE database using 'patmatmotifs' from EMBOSS."+end)
      print(green+"\n1. The selected 'patmatmotifs' file(s) which contain motif(s) will be generated in your directory. You can check it(them) as you like.\n"+end)
      file1=open('unaligned.fa').read().rstrip().split('\n')
      # Build up a dict
      seq={}
      for line in file1:
          if line.startswith('>'):
             name=line.replace('>','')
             seq[name]=''
          else:
             seq[name]+=line.replace('\n','').strip()
      # Determine whether any known motifs (domains) are associatd with this subset of of sequences
      motifs_total=[]
      keys=[]
      for n in seq.keys():
          keys.append(n)
      # For protein sequences whose number is no more than 250: Write one sequence each time to a new file.
      counter=1
      for m in keys:
          outfile=open('out_file','w')
          outfile.write('>')
          outfile.write(m)
          outfile.write('\n')
          outfile.write(seq[m])
          outfile.write('\n')
          outfile.close()
          filename='{}{}'.format(counter,'_patmatmotifs.report')
          # Use 'patmatmotifs' from EMBOSS to scan the subset of protein sequences
          subprocess.call('patmatmotifs -sequence {} -outfile {}'.format('out_file',filename), shell=True)
          # Loop through the 'patmatmotifs' files and tell users about the information about the found motif(s)
          for line in open(filename):
              motif=re.search("Motif = (.+)",line)
              if motif:
                 print(purple+"A motif found in this protein sequence."+end)
                 motifs_total.append(motif.group(1))
                 counter += 1
      motifs_set=list(set(motifs_total))
      motif_num=len(motifs_set)
      # Determine the number of motif(s) and tell users about the information about the found motif(s)
      print(green+"\nInformation about Motif(s):"+end)
      if motif_num==0:
         print("\nThere are "+red+"no"+end+" known motifs found to be associated with this subset of sequences.")
      else:
         print("\n(1) The motif(s) found is/are: ")
         print("\n"+purple+str(motifs_set)+end)
         print("\n(2) "+purple+str(motif_num)+end+" motif(s) is/are found to be associated with this subset of sequences.")               
   else:
      print ("\nAs the number of hits is more than 250, only 250 most similar sequences will be selected for the conservation analysis and plotting.\n")    
      # Part 2: Select 250 most similar sequenecs
      m=0   
      for line2 in blast2.iloc[:,1]:
          headers_250 = line2
          hits_250 += headers_250 + "\n"
          m=m+1
          if m > 249:
             break 
          else:
             continue
      # Ask users if they want to have a look at the 250 sequences
      # Use panda?
      while True:
          choice14=input(cyan+"\nDo you want to have a look at the selected 250 most similar sequences? (y/n)): "+end)
          if choice14.lower() == 'y':
             print("\nThe 250 most similar sequences: \n")
             print(hits_250)
             break
          else:
             if choice14.lower() == 'n':
                break
             else:
                print(red+"\nERROR: You did't type in the corrected format."+end+yellow+" \nwarning:You can only type either 'y' or 'n'. Please try again!"+end)
                continue
      hits_250_split=hits_250.rstrip('\n').split('\n')
      # Put the 250 accession numbers to a string
      accn=','.join(hits_250_split)
      # Put the 250 sequences to a fasta file
      unaligned_250=subprocess.call('efetch -db protein -id "{}" -format fasta > unaligned_250.fa'.format(accn), shell=True)
      # Align the 250 sequences using clustalo
      clustalo_results('unaligned_250.fa','aligned_250.msf')
      # For those sequences whose number is over 250: Draw a plot of protein conservation based on the alignment similarities
      print(green+"\n3. Draw a plot of protein conservation based on the alignment similarities by plotcon using EMBOSS.\n"+end)
      subprocess.call('plotcon -sequences {} -winsize 4 -graph svg'.format('aligned_250.msf'), shell=True)
      print("\nNow the plot has been successfully created and can be seen in 'plotcon.svg'")
# Part 3: For protein sequences whose number is more than 250: Scan protein sequence(s) with motifs from the PROSITE database
      print(green+"\nPart 3: Scan protein sequence(s) with motifs from the PROSITE database using 'patmatmotifs' from EMBOSS."+end)
      print("\nThe selected 'patmatmotifs' file(s) which contain motif(s) will be generated in your directory. You can check it(them) as you like.\n")
      file2=open('unaligned_250.fa').read().rstrip().split('\n')
      # Build up a dict 
      seq={}
      for line in file2:
          if line.startswith('>'):
             name=line.replace('>','')
             seq[name]=''
          else:
             seq[name]+=line.replace('\n','').strip()
      # Determine whether any known motifs (domains) are associatd with this subset of of sequences
      motifs_total=[]
      keys=[]
      for n in seq.keys():
          keys.append(n)
      # Write one sequence each time to a new file.
      counter=1
      for m in keys:
          outfile=open('out_file','w')
          outfile.write('>')
          outfile.write(m)
          outfile.write('\n')
          outfile.write(seq[m])
          outfile.write('\n')
          outfile.close()
          filename='{}{}'.format(counter,'_patmatmotifs.report')
          # Use 'patmatmotifs' from EMBOSS to scan the subset of protein sequences
          subprocess.call('patmatmotifs -sequence {} -outfile {}'.format('out_file',filename), shell=True)
          # Loop through the 'patmatmotifs' files and tell users about the information about the found motif(s)
          for line in open(filename):
              motif=re.search("Motif = (.+)",line)
              if motif:
                 print(purple+"A motif found in this protein sequence.\n"+end)
                 motifs_total.append(motif.group(1))
                 counter += 1
      motifs_set=list(set(motifs_total))
      motif_num=len(motifs_set)
      # Determine the number of motif(s) and tell users about the information about the found motif(s)
      print(green+"\nInformation about Motif(s)."+end)
      if motif_num==0:
         print("\nThere are"+red+" no "+end+"known motifs found to be associated with this subset of sequences.")
      else:
         print("\nThe motif(s) found is/are: ")
         print("\n"+purple+str(motifs_set)+end)
         print("\n"+purple+str(motif_num)+end+" motif(s) is/are found to be associated with this subset of sequences.")



##################################CHECK! Other analysis ('wildcard')
# Part 4: 'Wildcard': Other analysis to the output
print(green+"\nPart 4: 'Wildcard': Other analysis to the output."+end)
# 1. Prettyplot
print(cyan+"\n1. Use 'prettyplot' from EMBOSS to draw a plot of the input sequence alignment. The sequences are rendered in pretty formatting on the specified graphics device. Drawing options control the appearance of the image, such as boxes, colour and shading for highlighting conserved regions."+cyan)
subprocess.call('prettyplot -sequences {} -graph svg'.format('aligned.msf'), shell=True)
print(cyan+"\nYou can now check your beautiful svg file on your server."+end)

# 2. Infoalign: Display basic information about a multiple sequence alignment
print(cyan+"\n2. infoalign displays on screen basic information about sequences in an input multiple sequence alignment. This includes the sequences' USA, name, two measures of length, counts of gaps, and numbers of identical, similar and different residues or bases in this sequence when compared to a reference sequence, together with a simple statistic of the % change between the reference sequence and this sequence. Any combination of these records is easily selected or unselected for display. The same information may be written to an output file which (optionally) may be formatted in an HTML table.\n"+end)
subprocess.call('infoalign -sequence {} -outfile {}'.format('aligned.msf','multiple_seq.infoalign'), shell=True)
print(cyan+"\nYou can now check the multi_seq.infoalign file on your server."+end)
print(green+"\nAll of the analysis is done! \n\nSee you next time. Hope you have a nice day!\n"+end)