# xtrct_grid_tools

This tooling builds a docker image wrapping HYSPLIT's `xtrct_grid` subroutine, enabling extraction of spatial subdomains from ARL packed binary meteorological data files. 

## Installation

Fetch the latest image using: `docker pull benfasoli/xtrct-grid`

## Usage

```bash
export INPUT_DIR=$(pwd)
export OUTPUT_DIR=$(pwd)
docker run \
    -v $INPUT_DIR:/input \
    -v $OUTPUT_DIR:/output \
    benfasoli/xtrct-grid \
    --input=hysplit.20150811.06z.hrrra \
    --output=output.arl \
    --xmin=-112 \
    --xmax=-111 \
    --ymin=40 \
    --ymax=41
```
