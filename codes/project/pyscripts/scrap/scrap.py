import requests
from bs4 import BeautifulSoup
import html5lib


class Internshala:
    url="https://internshala.com/internships/"

    def get_data_from_content(self,content):
        """
        internship_name:Inside Sales Specialist
        company_name:Skill-Lync
        location: Hyderabad, Chennai, Delhi, Bangalore
        upload_duration:6 days ago
        CTC:3 - 4.5 LPA
        type: Fresher Job
        apply_link: "/job/detail/inside-sales-specialist-fresher-jobs-in-multiple-locations-at-skill-lync1676529765"
        """
        data=dict()
        data["internship_name"]=content.find("a",class_="view_detail_button").get_text()
        data["company_name"]=content.find("a",class_="link_display_like_text view_detail_button").get_text()
        data["location"]=content.find("a",class_="location_link view_detail_button").get_text()
        data["upload_duration"]=content.find("div",class_="posted_by_container").get_text()
        data["CTC"]=content.find("span",class_="stipend").get_text()
        data["type"]=content.find("div",class_="status status-small status-inactive").get_text()
        data["apply_link"]=content.find_all("div",class_="btn btn-primary b2b_apply_now")[0].get("data-redirect_url")
        return data
    
    def get_container(self,url):
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html.parser") 
        container=soup.find("div",id="internship_list_container_1")
        return container
    
    def get_internship_data(self):
        container=self.get_container(self.url)
        contents=container.find_all("div",class_="container-fluid")  
        data=list()
        start=1
        end=len(contents)
        for i in range(1,end,1):
            try:
                data.append(self.get_data_from_content(contents[i]))
            except:
                continue
        return data




class Scrap:
    #variables
    file_path="./codes/project/pyscripts/scrap/test.txt"
    #methods
    def scrap_from_internshala(self):
        inter=Internshala()
        file=open(self.file_path,"w")
        file.write(inter.get_internship_data())
        # return inter.get_internship_data()


sc=Scrap()
sc.scrap_from_internshala()

        