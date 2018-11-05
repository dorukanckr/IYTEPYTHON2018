text = """
As described previously, the captured views provide us two important data: 1) 
silhouettes of the object from different views, which define the visual hull of the object, and 
2) ray-ray correspondences before and after rays intersecting with the object, which correlate to light 
refraction paths and surface geometry details.
"""

a=text.replace("," , "")
b=a.replace(":" , "")
c=b.replace("1)" , "")
d=c.replace("2)" , "")

print(d)