import requests, m3u8

# list of link to .m3u8 files, extracted from web page
video_list = []


def video_downloader(filename, url):
	m3u8_url = requests.get(url)
	m3u8_master = m3u8.loads(m3u8_url.text)				# extracring links to stream resolutions (320/640/720p etc.)
	file_url = m3u8_master.data['playlists'][2]['uri']	# accessing 720p resolution. Verify before running the stream calling
	r = requests.get(file_url)							
	playlist = m3u8.loads(r2.text)						# exctracting urls for stream segments

	with open(f'{filename}.ts', 'wb') as f:					# concatenating binary data in .ts file from segment requests
		for segment in playlist.data['segments']:
			url = segment['uri']
			r3 = requests.get(url)
			f.write(r3.content)

for idx, url in enumerate(video_list):
	video_downloader(idx, url)