from conan import ConanFile
from conan.tools.files import get, copy
from os.path import join

required_conan_version = ">=1.43.0"


class RapidFuzzConan(ConanFile):
    name = "rapidfuzz"
    description = "Rapid fuzzy string matching in C++ using the Levenshtein Distance"
    topics = ("cpp", "levenshtein", "string-matching", "string-similarity", "string-comparison")
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/maxbachmann/rapidfuzz-cpp"
    license = "MIT"
    no_copy_source = True

    def source(self):
        get(self, **self.conan_data["sources"][self.version], strip_root=True)

    def package(self):
        copy(self, "LICENSE", self.source_folder, join(self.package_folder, "licenses"))
        copy(self, "rapidfuzz/*.hpp", self.source_folder, join(self.package_folder, "include"))
        copy(self, "rapidfuzz/*.impl", self.source_folder, join(self.package_folder, "include"))

    def package_id(self):
        self.info.clear()
