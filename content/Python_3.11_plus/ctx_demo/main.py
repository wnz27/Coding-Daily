from contextvars import copy_context, ContextVar

if __name__ == "__main__":
    var = ContextVar('var')
    var.set('spam')

    def main():
        # 'var' was set to 'spam' before
        # calling 'copy_context()' and 'ctx.run(main)', so:
        # var.get() == ctx[var] == 'spam'

        var.set('ham')

        # Now, after setting 'var' to 'ham':
        # var.get() == ctx[var] == 'ham'

    ctx = copy_context()

    # Any changes that the 'main' function makes to 'var'
    # will be contained in 'ctx'.
    ctx.run(main)

    # The 'main()' function was run in the 'ctx' context,
    # so changes to 'var' are contained in it:
    # ctx[var] == 'ham'
    print(ctx[var] == 'ham')

    # However, outside of 'ctx', 'var' is still set to 'spam':
    print(var.get() == 'spam')
    pass
