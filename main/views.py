from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
import cv2
import extcolors

from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from colormap import rgb2hex
   
    

    
# --- view for home
class Home(View):
    def get(self, request):
        return render(request, 'index.html')
    
    # -- sending post request (get data)
    def post(self, request):
        # -- check if post is well done
        try:
            # -- getting data from the html
            numWidth = request.POST.get('width')
            numHeight = request.POST.get('height')
            
            # -- checking if the file picked
            if request.FILES['imagePanel']:

                ##########
                #  
                imageFile = request.FILES['imagePanel'].name

                output_width = 900                   #set the output size in pexels
                img = Image.open(imageFile)
                wpercent = (output_width/float(img.size[0]))
                hsize = round(int((float(img.size[1])*float(wpercent))))
                img = img.resize((output_width,hsize), Image.ANTIALIAS)

                #prefixing img name then save
                resize_name = 'resize_' + imageFile  #the resized image name
                img.save(resize_name)                 #output location can be specified before resize_name
 
                img_url = resize_name

                ##########
                # 

                colors_x = extcolors.extract_from_path(img_url, tolerance = 12, limit = 12)

                ##########
                # 
                def color_to_df(input):
                    colours_pre_list = str(input).replace('([(','').split(', (')[0:-1]
                    df_rgb = [i.split('), ')[0] + ')' for i in colours_pre_list]
                    df_percent = [i.split('), ')[1].replace(')','') for i in colours_pre_list]
                    
                    #convert RGB to HEX code
                    df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(","")),
                                        int(i.split(", ")[1]),
                                        int(i.split(", ")[2].replace(")",""))) for i in df_rgb]
                    
                    # We assign the datasets generated to their column names
                    df = pd.DataFrame(zip(df_color_up, df_percent), columns = ['c_code','occurence'])
                    return df

                df_color = color_to_df(colors_x)
                ##########
                # 


                # Plot a donut chart to visualize the result

                list_color = list(df_color['c_code'])
                list_precent = [int(i) for i in list(df_color['occurence'])]
                text_c = [c + ' ' + str(round(p*100/sum(list_precent),1)) +'%' for c, p in zip(list_color,
                                                                                            list_precent)]
                fig, ax = plt.subplots(figsize=(90,90),dpi=10)
                wedges, text = ax.pie(list_precent,
                                    labels= text_c,
                                    labeldistance= 1.05,
                                    colors = list_color,
                                    textprops={'fontsize': 120, 'color':'black'}
                                    )
                plt.setp(wedges, width=0.3)

                # #create space in the center
                plt.setp(wedges, width=0.36)

                ax.set_aspect("equal")
                fig.set_facecolor('white')
                plt.show()

                ##########
                # 
                
                return redirect('color')
                # return redirect('color', request, {'img_url':img_url})
            else:
                messages.WARNING(request, 'Image picker faild, Please try again')
                return render(request, 'index.html')
        except:
            messages.WARNING(request, 'Invalid Form, Please try again')
            return render(request, 'index.html')
        




class ColorAnalysisView(View):
    def get(self, request):
        return render(request, 'color.html')
    
    # -- sending post request (get data)
    def post(self, request):
        # -- check if post is well done
        try:
            # -- getting data from the html
            colList = request.POST.getlist('flexRadioDefault[]')
            return redirect('result')
        except:
            messages.WARNING(request, 'Invalid Form, Please try again')
            return render(request, 'color.html')
    
    



# --- view for output
class Output(View):
    def get(self, request):
        cols = {'Nugget H','Sill H','Range H','Nugget V','Sill V','Range V'}
        context = {
            'cols': cols
        }
        return render(request, 'output.html', context)
    
    
    def post(self, request):
        return render(request, 'output.html')
