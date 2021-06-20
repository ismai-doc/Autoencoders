# Autoencoders

the autoencoder will encode the input distribution into a low-dimensional tensor,
which takes the form of a vector. This will approximate the hidden structure
that is commonly referred to as the latent representation, code, or vector. This
process constitutes the encoding part. The latent vector will then be decoded by
the decoder part to recover the original input.

They're a key tool in understanding the advanced topics of deep learning as
they give us a low-dimensional representation of data that is suitable for density
estimation.


the an autoencoder has two operators, these being:

• Encoder: This transforms the input, x, into a low-dimensional latent vector, z = f(x) . Since the latent vector is of low dimension, the encoder is forced
to learn only the most important features of the input data.

• Decoder: This tries to recover the input from the latent vector, g(z) =x'.  Although the latent vector has a low dimension, it has a sufficient size to allow
the decoder to recover the input data.

The goal of the decoder is to make x' as close as possible to x. Generally, both the
encoder and decoder are non-linear functions.
