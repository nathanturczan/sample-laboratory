# sample-laboratory
sample lab
set of tools for organizing samples in scale folders

creates folders for each pressing scale:
Diatonic (all 12 transpositions),
Acoustic (all 12 transpositions),
Octatonic (all 3 transpositions),
Whole-tone (both transpositions),
Harmonic minor (all 12 transpositions),
Harmonic major (all 12 transpositions),
Hexatonic (all 4 transpositions)

normalize all samples

update manifest containing sample information

a sample contains notes as a part of a chord or melody: [c, d, g, b]
the sample is saved in each scale folder that it is a subset of:
c_diatonic: [0, 2, 4, 5, 7, 9, 11],
g_diatonic,
f_acoustic,
c_harmonic_major,
g_harmonic_major,
c_harmonic minor,

the sample is transposed up by 1 semitone: [cs, ds, gs, bs]
and that transposed sample saved in each scale folder that it is a subset of:
cs_diatonic: [0, 1, 3, 5, 6, 8, 10],
gs_diatonic,
fs_acoustic,
cs_harmonic_major,
gs_harmonic_major,
cs_harmonic minor,

the sample is transposed down by 1 semitone: [cf, df, gf, bf]
and that transposed sample saved in each scale folder that it is a subset of:
b_diatonic: [1, 3, 4, 6, 8, 10, 11],
gf_diatonic,
e_acoustic,
b_harmonic_major,
gf_harmonic_major,
b_harmonic minor


