def main():
# =============================================================================
# SDR connection. Defined by single or multiple input and output streams.
# Passive radar typically uses two rx streams with an optional 3rd to calulate
# angle of arrivals.
#
# creates arrays of recieved multiple bladerf output streams.
# =============================================================================
    print("Starting SDR Connection")
    # TODO: Calculate angle of arrival on third rx stream with seperate hardware radio.
    # [rx1, rx2] = Sdr(NULL)


# PRINT RX STREAMS with plotting software. Include watterfall plots

# =============================================================================
# Radio DSP module. Defined by input streams adn optional functions useful for
# radio arrays.
#
# returns processed signal array?
# =============================================================================
    print("Starting DSP Modules for signal matching on input streams")
    # TODO: Calculate angle of arrival on third rx stream with seperate hardware radio.
    # dsp = Radio_Dsp(NULL)
    # Inpur Rx streams to Radio dsp
    # processed_signal = dsp.match_signal(rx1,rx2)


# =============================================================================
# Radio DSP module. Calculate doppler shift on rx streams given processed
# signal from previous step
# =============================================================================
    print("Calculate doppler shift")
    # TODO: Calculate angle of arrival on third rx stream with seperate hardware radio.
    # dsp = Radio_Dsp(NULL)
    # Inpur Rx streams to Radio dsp
    # processed_doppler_signal = dsp.doppler_shift(rx1,rx2,processed_signal)


# PRINT DOPPLER SHIFTED IN WAY THAT ILLUSTRATES BODY REFLECTIONS


if __name__ == "__main__":
    main()
