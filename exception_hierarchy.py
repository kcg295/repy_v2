"""

This file contains the exception hierarchy for repy. This allows repy modules
to import a single file to have access to all the defined exceptions.

"""


##### High-level, generic exceptions

class InternalRepyException (Exception):
  """
  All Fatal Repy Exceptions derive from this exception.
  This error should never make it to the user-code.
  """
  pass

class RepyException (Exception):
  """All Repy Exceptions derive from this exception."""
  pass

class RepyArgumentError (RepyException):
  """
  This Exception indicates that an argument was provided
  to a repy API as an in-appropriate type or value.
  """
  pass


##### Resource Related Exceptions

class ResourceUsageError (RepyException):
  """
  All Resource Usage Exceptions derive from this exception.
  """
  pass

class ResourceExhaustedError (ResourceUsageError):
  """
  This Exception indicates that a resource has been
  Exhausted, and that the operation has failed for that
  reason.
  """
  pass

##### File Related Exceptions

class FileError (RepyException):
  """All File-Related Exceptions derive from this exception."""
  pass

class FileNotFoundError (FileError):
  """
  This Exception indicates that a file which does not exist was
  used as an argument to a function expecting a real file.
  """
  pass

class FileInUseError (FileError):
  """
  This Exception indicates that a file which is in use was
  used as an argument to a function expecting the file to
  be un-used.
  """
  pass

class SeekPastEndOfFileError (FileError):
  """
  This Exception indicates that an attempt was made to
  seek past the end of a file.
  """
  pass

class FileClosedError (FileError):
  """
  This Exception indicates that the file is closed,
  and that the operation is therfor invalid.
  """
  pass

#####


