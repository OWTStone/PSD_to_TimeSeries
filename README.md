# PSD_to_TimeSeries
Generate a time series dataset from a given PSD <br>

Current input parameters are as follows:
<br>
PSD (2 vectors of frequency in Hz and power amplitude)
  <ul>
    <li>freq (Hz)</li>
    <li>amp (unit^2/Hz)</li>
<li>numPoints - number of time series samples generated (sample rate current set to 2X maximum frequency in PSD)</li>
  </ul>

Output is a vector of samples (time vector must be generated separately) with debug plots showing input spectrum, output signal, and comparision of output to requested input based on FFT performed at end of processing.<br>
