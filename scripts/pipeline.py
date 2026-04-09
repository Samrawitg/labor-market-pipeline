from extract_bls import extract_bls
from extract_fred import extract_fred
from extract_oews import extract_oews
from transform import transform_combined, transform_oews
from load import load_combined, load_oews

def run_pipeline():
    print("=" * 40)
    print("Starting labor market pipeline...")
    print("=" * 40)

    print("\n--- EXTRACT ---")
    extract_bls()
    extract_fred()
    extract_oews()

    print("\n--- TRANSFORM ---")
    transform_combined()
    transform_oews()

    print("\n--- LOAD ---")
    load_combined()
    load_oews()

    print("\n" + "=" * 40)
    print("Pipeline complete!")
    print("=" * 40)

if __name__ == "__main__":
    run_pipeline()