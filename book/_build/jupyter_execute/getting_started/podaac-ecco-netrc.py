#!/usr/bin/env python
# coding: utf-8

# # PO DAAC Authentication Example

# **Note this is currently copied from <https://github.com/podaac/ECCO/blob/main/Data_Access/local_bulk_download_and_open_in_py3.ipynb> as a starting point and will be refined** 
# 
# <img src="https://podaac.jpl.nasa.gov/sites/default/files/mission_themes/featured_image/%20Estimating-the-Circulation-and-Climate-of-the-Ocean-ECCO-opt2.jpg" />
# 
# 
# ### Configure your *.netrc* file
# 
# Good idea to back up your existing netrc file, if you have one. And while youre at it check for these entries because they might exist in there already:

# In[1]:


get_ipython().run_line_magic('cp', '~/.netrc ~/bak.netrc')

get_ipython().run_line_magic('cat', '~/.netrc | grep \'.earthdata.nasa.gov\' | cut -f-5 -d" "')


# >Add entries to your netrc for these two *earthdata.nasa.gov* sub domains, at a minimum:
# >```
# machine urs.earthdata.nasa.gov login jmcnelis password ***
# machine opendap.earthdata.nasa.gov login jmcnelis password ***
# >```
# >and replace `jmcnelis` and `***` with your Earthdata Login *username* and *password*, respectively...

# Replace `jmcnelis` and `***` with your Earthdata *username* and *password*, and then run the cell to _append_ these two lines to your netrc file, if one exists. Otherwise write them to a new one. (all set up by `-a`)

# In[2]:


get_ipython().run_cell_magic('file', '-a ~/.netrc', 'machine urs.earthdata.nasa.gov login jmcnelis password ***\nmachine opendap.earthdata.nasa.gov login jmcnelis password ***')


# Dump the netrc again sans passwords to confirm that it worked:

# In[3]:


get_ipython().system('cat ~/.netrc | grep \'.earthdata.nasa.gov\' | cut -f-5 -d" "')


# Finally, you need to make sure to limit access to the netrc file because it stores your plain text password. Simple on MacOS and Linux:

# In[4]:


get_ipython().system('chmod 0600 ~/.netrc')

