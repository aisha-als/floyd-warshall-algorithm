# floydwarshall

This is a Python package to use the Floyd-Warshall algorithm to calculate the distance matrix in an adjacency matrix.

This package uses a recursive version of the algorithm, re-written from the iterative version in the root folder of this package.

This package is written using PEP 8 guidelines.

## Table of Contents

- [Install](#Install)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](#License)

## Install

This package is written using `Python 3.11.7`.

To install this package use pip:
```sh
pip install git+https://github.com/aisha-als/floyd-warshall-algorithm.git
```

To install the dependencies use pip:
```sh
pip install -r requirements.txt
```

## Usage

### Performance Tests

Performance tests are run using `cProfile`. 

To run the performance tests, run the below command:
```sh
python tests/performance_test.py
```

### Unit Tests

Unit tests are run using `unittest`. 

To run the unit tests, run the below command:
```sh
python -m unittest
```

## Contributing

Please open a PR for contributions.

## License

MIT License.

See license in [LICENSE](floyd-warshall-algorithm/LICENSE)