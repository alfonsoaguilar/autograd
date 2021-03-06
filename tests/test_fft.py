from __future__ import absolute_import
import autograd.numpy as np
import autograd.numpy.random as npr
from autograd.util import *
from autograd import grad
from numpy.testing import assert_raises, assert_array_equal
npr.seed(1)

def test_fft():
    def fun(x): return to_scalar(np.fft.fft(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_fft_ortho():
    def fun(x): return to_scalar(np.fft.fft(x, norm='ortho'))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_fft_axis():
    def fun(x): return to_scalar(np.fft.fft(x, axis=0))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def match_complex(fft_fun, mat):
    # ensure hermitian by doing a fft
    if fft_fun.__name__.startswith('ir'):
        return getattr(np.fft, fft_fun.__name__[1:])(mat)
    else:
        return mat

def check_fft_n(fft_fun, D, n):
    def fun(x): return to_scalar(fft_fun(x, D + n))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    mat = npr.randn(D, D)
    mat = match_complex(fft_fun, mat)
    assert_array_equal(grad(fun)(mat).shape, mat.shape)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_fft_n_smaller(): check_fft_n(np.fft.fft, 5, -2)
def test_fft_n_bigger(): check_fft_n(np.fft.fft, 5, 2)
def test_ifft_n_smaller(): check_fft_n(np.fft.ifft, 5, -2)
def test_ifft_n_bigger(): check_fft_n(np.fft.ifft, 5, 2)

def test_rfft_n_smaller(): check_fft_n(np.fft.rfft, 4, -2)
def test_rfft_n_bigger(): check_fft_n(np.fft.rfft, 4, 2)
def test_irfft_n_smaller(): check_fft_n(np.fft.irfft, 4, -2)
def test_irfft_n_bigger(): check_fft_n(np.fft.irfft, 4, 2)

def check_fft_s(fft_fun, D):
   def fun(x): return to_scalar(fft_fun(x, s=s, axes=axes))
   d_fun = lambda x : to_scalar(grad(fun)(x))

   mat = npr.randn(D,D,D) / 10.0
   mat = match_complex(fft_fun, mat)
   s = [D + 2, D - 2]
   axes = [0,2]

   check_grads(fun, mat)
   check_grads(d_fun, mat)

def test_fft2_s():  check_fft_s(np.fft.fft2, 5)
def test_ifft2_s(): check_fft_s(np.fft.ifft2, 5)
def test_fftn_s():  check_fft_s(np.fft.fftn, 5)
def test_ifftn_s(): check_fft_s(np.fft.ifftn, 5)

def test_rfft2_s():  check_fft_s(np.fft.rfft2, 4)
def test_irfft2_s(): check_fft_s(np.fft.irfft2, 4)
def test_rfftn_s():  check_fft_s(np.fft.rfftn, 4)
def test_irfftn_s(): check_fft_s(np.fft.irfftn, 4)

## TODO: fft gradient not implemented for repeated axes
# def test_fft_repeated_axis():
#     D = 5
#     for fft_fun in (np.fft.fft2,np.fft.ifft2,np.fft.fftn, np.fft.ifftn):
#        def fun(x): return to_scalar(fft_fun(x, s=s, axes=axes))
#        d_fun = lambda x : to_scalar(grad(fun)(x))

#        mat = npr.randn(D,D,D) / 10.0
#        s = [D + 2, D - 2]
#        axes = [0,0]

#        check_grads(fun, mat)
#        check_grads(d_fun, mat)

def test_ifft():
    def fun(x): return to_scalar(np.fft.ifft(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_fft2():
    def fun(x): return to_scalar(np.fft.fft2(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_ifft2():
    def fun(x): return to_scalar(np.fft.ifft2(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_fftn():
    def fun(x): return to_scalar(np.fft.fftn(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_ifftn():
    def fun(x): return to_scalar(np.fft.ifftn(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_rfft():
    def fun(x): return to_scalar(np.fft.rfft(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_rfft_ortho():
    def fun(x): return to_scalar(np.fft.rfft(x, norm='ortho'))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_rfft_axes():
    def fun(x): return to_scalar(np.fft.rfft(x, axis=0))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_irfft():
    def fun(x): return to_scalar(np.fft.irfft(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D) / 10.0
    # ensure hermitian by doing a fft
    mat = np.fft.rfft(mat)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_irfft_ortho():
    def fun(x): return to_scalar(np.fft.irfft(x, norm='ortho'))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D) / 10.0
    # ensure hermitian by doing a fft
    mat = np.fft.rfft(mat)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_rfft2():
    def fun(x): return to_scalar(np.fft.rfft2(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_irfft2():
    def fun(x): return to_scalar(np.fft.irfft2(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D) / 10.0
    # ensure hermitian by doing a fft
    mat = np.fft.rfft2(mat)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_rfftn():
    def fun(x): return to_scalar(np.fft.rfftn(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_rfftn_odd_not_implemented():
    def fun(x): return to_scalar(np.fft.rfftn(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D, D) / 10.0
    assert_raises(NotImplementedError, check_grads, fun, mat)

def test_rfftn_subset():
    def fun(x): return to_scalar(np.fft.rfftn(x)[(0, 1, 0), (3, 3, 2)])
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_rfftn_axes():
    def fun(x): return to_scalar(np.fft.rfftn(x, axes=(0, 2)))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_irfftn():
    def fun(x): return to_scalar(np.fft.irfftn(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D, D) / 10.0
    # ensure hermitian by doing a fft
    mat = np.fft.rfftn(mat)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_irfftn_subset():
    def fun(x): return to_scalar(np.fft.irfftn(x)[(0, 1, 0), (3, 3, 2)])
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D, D) / 10.0
    # ensure hermitian by doing a fft
    mat = np.fft.rfftn(mat)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_fftshift():
    def fun(x): return to_scalar(np.fft.fftshift(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_fftshift_even():
    def fun(x): return to_scalar(np.fft.fftshift(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_fftshift_axes():
    def fun(x): return to_scalar(np.fft.fftshift(x, axes=1))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D) / 10.0
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_ifftshift():
    def fun(x): return to_scalar(np.fft.ifftshift(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_ifftshift_even():
    def fun(x): return to_scalar(np.fft.ifftshift(x))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 4
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)

def test_ifftshift_axes():
    def fun(x): return to_scalar(np.fft.ifftshift(x, axes=1))
    d_fun = lambda x : to_scalar(grad(fun)(x))
    D = 5
    mat = npr.randn(D, D)
    check_grads(fun, mat)
    check_grads(d_fun, mat)
