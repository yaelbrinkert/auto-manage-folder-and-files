# auto-create-folder

This small python script detects automatically sub-folders in folders, to access the very end of the path. From here, it will look at all files, create folders from files name, and move the file to his corresponding folder.

Let's say we have a folder that contains many images. Those images should have a corresponding JSON attached to it (having informations concerning the image). I want don't want my folder to become a mess, having all JSONs and images at the same place.

But, I'm lazy, I don't want to manually create a folder to host my image and his JSON.

Here goes my beautiful script ✨

## What it does, but explained by a pretty schema

Look at our structure for the moment :

- Chapter 3/
- - Season 4/
- - - 24.00.jpg
- - - 24.10.jpg
- - - 24.20.jpg
- - - 24.00.json
- - - 24.10.json
- - - 24.20.json
- - - ...

That's not very cool is it ? This folder structure ain't easy to use and navigate through. Let's fix this, using the script.\
Here is what results from using it :

- Chapter 3/
- - Season 4/
- - - 24.00/
- - - - 24.00.jpg
- - - - 24.00.json
- - - 24.10/
- - - - 24.10.jpg
- - - - 24.10.json
- - - 24.20/
- - - - 24.20.jpg
- - - - 24.20.json

Much better, isn't it ? What did we do here exactly ?\
We created new folders from files name (24.00.jpg became a new folder, called : 24.00/), and moved the file 24.00.jpg to his corresponding folder called 24.00/.

## But how is it useful for me ?

It's not, I made this because I'm lazy. Although, if you have a very specific case where you need this script, don't mind using it, or adjusting it.

## I have an idea to make this even more helpful and interesting !

Don't mind telling me, I would love to hear your idea or advice, and would love to make this repo a bit more helpful !\
Here is my discord if you want to discuss : yael#2898 (yaelou)
