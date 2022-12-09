package utils

type Result[T any] struct {
	data *T
	err  *error
}

func From[T any](t T, err error) Result[T] {
	if err != nil {
		return Result[T]{
			data: &t,
		}
	}

	return Result[T]{
		err: &err,
	}
}

func (r Result[T]) Unwrap() *T {
	if r.data != nil {
		return r.data
	}

	panic(r.err)
}

func JustRun[T any](f func() (T, error)) T {
	res, err := f()
    if err != nil {
      panic(err)
    }

    return res
}
