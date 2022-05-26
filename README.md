## Installation on Windows using Anaconda
```
conda create -n MoviePy_Split_Videoclips -y && conda activate MoviePy_Split_Videoclips && conda install python=3.9.7 -y
git clone https://github.com/alex1779/MoviePy_Split_Videoclips.git
cd MoviePy_Split_Videoclips
pip install -r requirements.txt


```
## For running
```
python main.py -i input/test.mp4 -p 5
```

## How Works

```
The -i parameter is the input path of the file to split, for example -i input/test.mp4
The parameter -p is the input of an integer and means the number of parts in which the original video will be divided, for example -p 5
```

![IMG](https://github.com/alex1779/MoviePy_Split_Videoclip/blob/master/img.jpg)
