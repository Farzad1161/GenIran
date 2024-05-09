#!/usr/bin/env python
# coding: utf-8

# In[3]:


Gene_name1 = 'Pten'
Gene_length1 = 16
Risk_assignment1 = 33.8
Gene_name2 = 'mTORC1'
Gene_length2 = 22
Risk_assignment2 = 47.7
Gene_name3 = 'mTORC2'
Gene_length3 = 23
Risk_assignment3 = 43.2
Is_DNA = True
Is_Protein = False
Is_Nucleotide = False
print(Gene_name1, Gene_name2, Gene_name3)
print(Gene_length1, Gene_length2, Gene_length3)
print(Risk_assignment1, Risk_assignment2, Risk_assignment3)
print(Is_DNA, Is_Protein, Is_Nucleotide)


# In[10]:


print(type(Gene_name1))
print(type(Gene_length1))
print(type(Risk_assignment1))
print(type(Is_DNA))


# In[11]:


print(str(Gene_length1), str(Gene_length2), str(Gene_length3))


# In[12]:


X = 456.354
print(int(X))


# In[3]:


Age = int(input('Enter your age: '))
print(Age*3)


# In[18]:


gene_ID = input('gene_ID: ')
Official_Symbol = input('Official Symbol: ')
Official_Full_Name = input('Official Full Name: ')
Isprotein_coding_or_not = input('Isprotein coding or not: ')
Summary = input('Summary: ')
Exon_count = input('Exon count: ')
Lineage = input('Lineage: ')
Coding_sequence = input('Coding sequence: ')


# In[19]:


print('The new record is constituted of:', "gene_ID:", gene_ID, ',' , "Official Symbol:", Official_Symbol, ',' , "Official Full Name:", Official_Full_Name, ',' , "Isprotein coding or not:", Isprotein_coding_or_not, ',' , "Summary:", Summary, ',' , "Exon count:", Exon_count, ',' , "Lineage:", Lineage, ',' , "Coding sequence:", Coding_sequence)

