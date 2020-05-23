# m3u8-downloader
Simple yet efficient m3u8 stream downloader
-----------------

To run the script you will require installing following dependecies:
`pip install requests`
`pip install m3u8`

Simple Python script to download .m3u8 stream binary data and write it in .ts file. Script utilises requests and m3u8 libraries. Before running the script check the resoulutio you want to download by using following commands:
```python
m3u8_url = requests.get(url)			# url to .m3u8 file
m3u8_master = m3u8.loads(m3u8_url.text)	# extracring links to stream resolutions (320/640/720p etc.)
>>> m3u8_master.data['playlists']		# display available resolutions to download
```
-----------------
To convert .ts file to .mp4, you will requrie to import subprocess library and call `'ffmpeg'` wrapper:
```python
>>> import subprocess

>>> subprocess.run(['ffmpeg', '-i', f'{filename}.ts', f'{filename}.mp4'])
```
