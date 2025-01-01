from pydub import AudioSegment
import os
import sys

def convert_m4a_to_wav(input_path, output_path=None):
    """
    Convert an M4A audio file to WAV format.
    
    Parameters:
    input_path (str): Path to the input M4A file
    output_path (str, optional): Path for the output WAV file. If not provided,
                                will use the same name as input with .wav extension
    
    Returns:
    str: Path to the converted file
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        # Generate output path if not provided
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + '.wav'
            
        # Load the audio file
        audio = AudioSegment.from_file(input_path, format="m4a")
        
        # Export as WAV
        audio.export(output_path, format="wav")
        
        print(f"Successfully converted {input_path} to {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error converting file: {str(e)}")
        return None

if __name__ == "__main__":
    # Handle command line arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py input_file.m4a [output_file.wav]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_m4a_to_wav(input_file, output_file)