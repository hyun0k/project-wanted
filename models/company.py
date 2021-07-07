from sqlalchemy.orm import relationship
from sqlalchemy     import Column, Integer, String, Boolean, DateTime, ForeignKey

from database       import db

class Company(db.Model):
    
    __tablename__ = "companies"
    
    id         = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=db.func.current_timestamp(), 
                                        index=False, 
                                        unique=False, 
                                        nullable=False)

    company_ko = relationship("CompanyKo", back_populates="company", uselist=False)
    company_en = relationship("CompanyEn", back_populates="company", uselist=False)
    company_ja = relationship("CompanyJa", back_populates="company", uselist=False)

    companies_tags = relationship("CompanyTag", back_populates="company")
    
    def __repr__(self) -> str:
        return "<Company({}, {})>".format(self.id, self.created_at)

class CompanyKo(db.Model):

    __tablename__ = "company_ko"

    id            = Column(Integer, primary_key=True)
    company_id    = Column(Integer, ForeignKey("companies.id"), nullable=False)
    language_code = Column(String(10), index=False, unique=False, nullable=False)
    name          = Column(String(45), index=False, unique=False, nullable=True)
    is_default    = Column(Boolean, index=False,default=False, nullable=False)

    company = relationship("Company", back_populates="company_ko")

    def __repr__(self) -> str:
        return "<CompanyKo({}, {}, {}, {}, {})>".format(self.id,
                                                        self.company_id, 
                                                        self.language_code,
                                                        self.name,
                                                        self.is_default)

class CompanyEn(db.Model):

    __tablename__ = "company_en"

    id            = Column(db.Integer, primary_key=True)
    company_id    = Column(db.Integer, ForeignKey("companies.id"), nullable=False)
    language_code = Column(db.String(10), index=False, unique=False, nullable=False)
    name          = Column(db.String(45), index=False, unique=False, nullable=True)
    is_default    = Column(db.Boolean, index=False,default=False, nullable=False)

    company = relationship("Company", back_populates="company_en")

    def __repr__(self) -> str:
        return "<CompanyEn({}, {}, {}, {}, {})>".format(self.id,
                                                        self.company_id,
                                                        self.language_code,
                                                        self.name,
                                                        self.is_default)

class CompanyJa(db.Model):

    __tablename__ = "company_ja"

    id            = Column(Integer, primary_key=True)
    company_id    = Column(Integer, ForeignKey("companies.id"), nullable=False)
    language_code = Column(String(10), index=False, unique=False, nullable=False)
    name          = Column(String(45), index=False, unique=False, nullable=True)
    is_default    = Column(Boolean, index=False,default=False, nullable=False)

    company = relationship("Company", back_populates="company_ja")

    def __repr__(self) -> str:
        return "<CompanyJa({}, {}, {}, {}, {})>".format(self.id, 
                                                        self.company_id,
                                                        self.language_code,
                                                        self.name,
                                                        self.is_default)

class Tag(db.Model):
    
    __tablename__ = "tags"
    
    id         = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=db.func.current_timestamp(), 
                                        index=False,
                                        unique=False, 
                                        nullable=False)

    tag_ko = relationship("TagKo", back_populates="tag", uselist=False)
    tag_en = relationship("TagEn", back_populates="tag", uselist=False)
    tag_ja = relationship("TagJa", back_populates="tag", uselist=False)
    
    tags_companies = relationship("CompanyTag", back_populates="tag")

    def __repr__(self) -> str:
        return "<Tag({}, {})>".format(self.id, self.created_at)

class TagKo(db.Model):

    __tablename__ = "tag_ko"

    id            = Column(Integer, primary_key=True)
    tag_id        = Column(Integer, ForeignKey("tags.id"), nullable=False)
    language_code = Column(String(10), index=False, unique=False, nullable=False)
    name          = Column(String(45), index=False, unique=False, nullable=True)
    is_default    = Column(Boolean, index=False,default=False, nullable=False)

    tag = relationship("Tag", back_populates="tag_ko")

    def __repr__(self) -> str:
        return "<TagKo({}, {}, {}, {}, {})>".format(self.id,
                                                    self.tag_id,
                                                    self.language_code,
                                                    self.name,
                                                    self.is_default)

class TagEn(db.Model):

    __tablename__ = "tag_en"

    id            = Column(Integer, primary_key=True)
    tag_id        = Column(Integer, ForeignKey("tags.id"), nullable=False)
    language_code = Column(String(10), index=False, unique=False, nullable=False)
    name          = Column(String(45), index=False, unique=False, nullable=True)
    is_default    = Column(Boolean, index=False,default=False, nullable=False)

    tag = relationship("Tag", back_populates="tag_en")

    def __repr__(self) -> str:
        return "<TagEn({}, {}, {}, {}, {})>".format(self.id,
                                                    self.tag_id,
                                                    self.language_code,
                                                    self.name,
                                                    self.is_default)

class TagJa(db.Model):

    __tablename__ = "tag_ja"

    id            = Column(Integer, primary_key=True)
    tag_id        = Column(Integer, ForeignKey("tags.id"), nullable=False)
    language_code = Column(String(10), index=False, unique=False, nullable=False)
    name          = Column(String(45), index=False, unique=False, nullable=True)
    is_default    = Column(Boolean, index=False,default=False, nullable=False)

    tag = relationship("Tag", back_populates="tag_ja")

    def __repr__(self) -> str:
        return "<TagJa({}, {}, {}, {}, {})>".format(self.id,
                                                    self.tag_id,
                                                    self.language_code,
                                                    self.name,
                                                    self.is_default)

class CompanyTag(db.Model):

    __tablename__ = "companies_tags"

    id         = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    tag_id     = Column(Integer, ForeignKey("tags.id"), nullable=False)

    company = relationship("Company", back_populates="companies_tags")
    tag     = relationship("Tag", back_populates="tags_companies")

    def __repr__(self) -> str:
        return "<TagJa({}, {}, {})>".format(self.id,
                                            self.company_id,
                                            self.tag_id)
