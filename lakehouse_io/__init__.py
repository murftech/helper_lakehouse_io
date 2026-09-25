"""Engine read/write mechanics - one write path per format/engine combination,
side by side (pyarrow/parquet, pyiceberg/Sail, sparkiceberg/JVM, sparkdelta/JVM,
deltalake local-JVM-free), plus shared_schema_guards.py which several of them
import from. Namespace only - no re-exports, same convention as providers/__init__.py.
"""
