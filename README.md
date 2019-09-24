# xtrct_grid_tools

This tooling builds a docker image wrapping HYSPLIT's `xtrct_grid` subroutine, enabling extraction of spatial subdomains from ARL packed binary meteorological data files. 

## Installation

Fetch the latest image using: `docker pull benfasoli/xtrct-grid`

## Usage

```bash
> ./entrypoint.py --help

usage: entrypoint.py [-h] -l XMIN -r XMAX -b YMIN -t YMAX -i INPUT -o OUTPUT
                     [--input_dir INPUT_DIR] [--output_dir OUTPUT_DIR]
                     [--levels LEVELS]

Extract spatial subdomain from ARL packed file.

optional arguments:
  -h, --help            show this help message and exit
  -l XMIN, --xmin XMIN  minimum x coordinate of subdomain
  -r XMAX, --xmax XMAX  maximum x coordinate of subdomain
  -b YMIN, --ymin YMIN  minimum y coordinate of subdomain
  -t YMAX, --ymax YMAX  maximum y coordinate of subdomain
  -i INPUT, --input INPUT
                        input data file name without path
  -o OUTPUT, --output OUTPUT
                        output data file name
  --input_dir INPUT_DIR
                        mount location for input data volume
  --output_dir OUTPUT_DIR
                        mount location for output data volume
  --levels LEVELS       vertical levels to extract
```

Executing via command line - 

```bash
export INPUT_DIR=$(pwd)
export OUTPUT_DIR=$(pwd)
./entrypoint.py \
    --input_dir=$INPUT_DIR \
    --input=hysplit.20150811.06z.hrrra \
    --output_dir=$OUTPUT_DIR \
    --output=output.arl \
    --xmin=-112 \
    --xmax=-111 \
    --ymin=40 \
    --ymax=41
```    

Executing with docker or udocker -

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
