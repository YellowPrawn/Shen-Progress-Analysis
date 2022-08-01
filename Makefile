# download and summarize data
all : data/summary.data

# download and summarize data
data/summary.data : ./src/get_shroom_summary.py
	python src/get_shroom_summary.py "na1" "PrawnJ" 100

# remove all created files
clean :
	rm -f data/summary.data