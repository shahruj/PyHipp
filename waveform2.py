import PyHipp as pyh
import DataProcessingTools as DPT
import numpy as np
import matplotlib.pyplot as plt
import hickle as hkl
import os
class Waveform(DPT.DPObject):
    # Please change the class name according to your needs
    filename = 'waveform.hkl'  # this is the filename that will be saved if it's run with saveLevel=1
    argsList = []  # these is where arguments used in the creation of the object are listed
    level = 'channel'  # this is the level that this object will be created in

    def __init__(self, *args, **kwargs):
        DPT.DPObject.__init__(self, *args, **kwargs)

    def create(self, *args, **kwargs):
        pwd = os.path.normpath(os.getcwd());
        # 'channelxxx, xxx is the number of the channel'
        self.channel_filename = [os.path.basename(pwd)]  
        template_fileanme = os.path.join(
        DPT.levels.resolve_level('day', self.channel_filename[0]),'mountains', self.channel_filename[0], 'output', 'templates.hkl')
        # this function will be called once to create this waveform object
        templates=hkl.load(template_fileanme)
        aname = DPT.levels.normpath(os.path.dirname(pwd))
        self.array_dict = dict()
        self.array_dict[aname] = 0
        self.numSets = 1
        self.current_plot_type = None
        # one neat property of Object-Oriented Programming (OOP) structure is that 
        # you can create some field-value pairs that can be called and updated 
        # in all functions of the object, if you specify the function properly.
        # The only thing that you need to do is to instantiate those fields in
        # this function with the prefix 'self.', then you can call them and 
        # edit them in all the other functions that have the first input argument
        # being 'self'
        #
        # For exmample, if you instantiate a field-value pair:
        # self.name = IronMan
        #
        # You can then call them or edit them in other functions:
        # def get_name(self):
        #    print(self.name)
        #
        # def set_name(self, new_name):
        #    self.name = new_name
        #
        # In this way, you don't need to return and pass in so many arguments 
        # across different functions anymore :)
        
        
        # The following is some hints of the things-to-do:
        
        # read the mountainsort template files
        self.data = [np.squeeze(templates)]
        dim=self.data.shape
        
        
        # .........................................
        # ..................code...................
        # .........................................
        
        
        # check on the mountainsort template data and create a DPT object accordingly
        # Example:
        if dim[0] != 0:
            # create object if data is not empty
            DPT.DPObject.create(self, *args, **kwargs)
        else:
            # create empty object if data is empty
            DPT.DPObject.create(self, dirs=[], *args, **kwargs)            
        
    def append(self, wf):
        DPT.DPObject.append(self, wf)
        self.data = self.data + wf.data
        for ar in wf.array_dict:
            self.array_dict[ar] = self.numSets
        self.numSets += 1

 
