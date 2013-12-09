python setup.py build_ext --inplace


building 'bilinearinterp' extension
C compiler: clang -fno-strict-aliasing -fno-common -dynamic -g -Os -pipe -fno-common -fno-strict-aliasing -fwrapv -mno-fused-madd -DENABLE_DTRACE -DMACOSX -DNDEBUG -Wall -Wstrict-prototypes -Wshorten-64-to-32 -DNDEBUG -g -Os -Wall -Wstrict-prototypes -DENABLE_DTRACE -arch i386 -arch x86_64 -pipe

compile options: '-I/Library/Python/2.7/site-packages/numpy-override/numpy/core/include -I/System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c'
clang: bilinearinterp.c
clang: warning: argument unused during compilation: '-mno-fused-madd'
In file included from bilinearinterp.c:5:
In file included from /Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/arrayobject.h:15:
In file included from /Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarrayobject.h:17:
In file included from /Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1728:
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/npy_deprecated_api.h:11:2: warning: "Using deprecated NumPy API, disable it by #defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
#warning "Using deprecated NumPy API, disable it by #defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
 ^
1 warning generated.
In file included from bilinearinterp.c:5:
In file included from /Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/arrayobject.h:15:
In file included from /Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarrayobject.h:17:
In file included from /Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1728:
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/npy_deprecated_api.h:11:2: warning: "Using deprecated NumPy API, disable it by #defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
#warning "Using deprecated NumPy API, disable it by #defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION"
 ^
bilinearinterp.c:132:11: warning: implicit conversion loses integer precision: 'npy_intp' (aka 'long') to 'int' [-Wshorten-64-to-32]
    inx = PyArray_DIM(input,0);
        ~ ^~~~~~~~~~~~~~~~~~~~
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1486:29: note: expanded from macro 'PyArray_DIM'
#define PyArray_DIM(obj,n) (PyArray_DIMS(obj)[n])
                            ^~~~~~~~~~~~~~~~~~~~
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1484:27: note: expanded from macro 'PyArray_DIMS'
#define PyArray_DIMS(obj) (((PyArrayObject_fields *)(obj))->dimensions)
                          ^
bilinearinterp.c:133:11: warning: implicit conversion loses integer precision: 'npy_intp' (aka 'long') to 'int' [-Wshorten-64-to-32]
    iny = PyArray_DIM(input,1);
        ~ ^~~~~~~~~~~~~~~~~~~~
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1486:29: note: expanded from macro 'PyArray_DIM'
#define PyArray_DIM(obj,n) (PyArray_DIMS(obj)[n])
                            ^~~~~~~~~~~~~~~~~~~~
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1484:27: note: expanded from macro 'PyArray_DIMS'
#define PyArray_DIMS(obj) (((PyArrayObject_fields *)(obj))->dimensions)
                          ^
bilinearinterp.c:134:11: warning: implicit conversion loses integer precision: 'npy_intp' (aka 'long') to 'int' [-Wshorten-64-to-32]
    onx = PyArray_DIM(output,0);
        ~ ^~~~~~~~~~~~~~~~~~~~~
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1486:29: note: expanded from macro 'PyArray_DIM'
#define PyArray_DIM(obj,n) (PyArray_DIMS(obj)[n])
                            ^~~~~~~~~~~~~~~~~~~~
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1484:27: note: expanded from macro 'PyArray_DIMS'
#define PyArray_DIMS(obj) (((PyArrayObject_fields *)(obj))->dimensions)
                          ^
bilinearinterp.c:135:11: warning: implicit conversion loses integer precision: 'npy_intp' (aka 'long') to 'int' [-Wshorten-64-to-32]
    ony = PyArray_DIM(output,1);
        ~ ^~~~~~~~~~~~~~~~~~~~~
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1486:29: note: expanded from macro 'PyArray_DIM'
#define PyArray_DIM(obj,n) (PyArray_DIMS(obj)[n])
                            ^~~~~~~~~~~~~~~~~~~~
/Library/Python/2.7/site-packages/numpy-override/numpy/core/include/numpy/ndarraytypes.h:1484:27: note: expanded from macro 'PyArray_DIMS'
#define PyArray_DIMS(obj) (((PyArrayObject_fields *)(obj))->dimensions)
                          ^
5 warnings generated.
clang -bundle -undefined dynamic_lookup -Wl,-F. -arch i386 -arch x86_64 build/temp.macosx-10.8-intel-2.7/bilinearinterp.o -o /Users/thomascampagne/Work/2D_filters/master/bilinearinterp/bilinearinterp.so

